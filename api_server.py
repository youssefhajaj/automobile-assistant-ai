from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel
from datetime import datetime
from llama_cpp import Llama
from typing import Optional, Dict, List
from fastapi.templating import Jinja2Templates
from fastapi import Request
import base64
import io
from PIL import Image
import torch
from ultralytics import YOLO
import cv2
import numpy as np
from collections import defaultdict
from rapidfuzz import fuzz, process
import re
import time

# Import keywords from external file
from keywords import GENERAL_CONVERSATION_KEYWORDS, AUTOMOBILE_KEYWORDS

# Import new modules
from obd_codes import OBD_CODES, get_obd_code_info, format_obd_response, search_obd_codes
from analytics import (
    log_conversation, detect_intent, learn_from_conversation,
    find_similar_question, get_analytics_summary, get_top_questions
)
from web_search import detect_search_intent, perform_search, search_duckduckgo, format_search_results

templates = Jinja2Templates(directory="templates")
app = FastAPI()

# Conversation memory storage
conversation_memory = defaultdict(list)

# Load Qwen2.5-32B-Instruct-Q5 (MAXIMIZED for RTX 4090 24GB)
model = Llama(
    model_path="/workspace/ai/Qwen2.5-32B-Instruct-Q5_K_M.gguf",
    n_gpu_layers=-1,         # All layers on GPU
    n_ctx=4096,              # 4K context (reduced to fit in VRAM)
    n_batch=256,             # Reduced batch size for 32B model
    n_threads=32,            # Use all CPU threads
    n_threads_batch=32,      # Batch processing threads
    verbose=False            # Clean logs
)

# Load YOLOv8 model
yolo_model = YOLO("/workspace/ai/best.pt")

def detect_obd_code(text: str) -> Optional[str]:
    """Detect OBD-II code in user message."""
    # Pattern for OBD codes: P0000, B0000, C0000, U0000
    # Also handles variations like P00002 (extra zeros) or p 0420 (with space)

    # First try standard format
    pattern = r'\b([PpBbCcUu])\s*[0]*([0-9]{4})\b'
    match = re.search(pattern, text)
    if match:
        prefix = match.group(1).upper()
        code = match.group(2)
        return f"{prefix}{code}"

    # Try with extra digits (P00002 -> P0002)
    pattern2 = r'\b([PpBbCcUu])[0]*([0-9]{3,5})\b'
    match2 = re.search(pattern2, text)
    if match2:
        prefix = match2.group(1).upper()
        digits = match2.group(2)
        # Normalize to 4 digits
        if len(digits) > 4:
            digits = digits[:4]
        elif len(digits) < 4:
            digits = digits.zfill(4)
        return f"{prefix}{digits}"

    return None

def correct_typos(text: str) -> str:
    """
    Correct common typos in user input using fuzzy matching.
    Handles misspellings of key terms like 'kounhany', automobile terms, etc.
    """
    # First, handle common phrase patterns
    text_lower = text.lower()

    # Fix "c est aoi" -> "c'est quoi" pattern
    phrase_corrections = [
        (r"c\s*est\s+aoi\b", "c'est quoi"),
        (r"c\s*est\s+qoi\b", "c'est quoi"),
        (r"c\s*est\s+koi\b", "c'est quoi"),
        (r"sver\b", "savez"),
        (r"sr\b", "sur"),
        (r"\bque vous sver\b", "que savez-vous"),
        (r"\bque vous savez\b", "que savez-vous"),
    ]

    for pattern, replacement in phrase_corrections:
        text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

    # Dictionary of correct spellings for fuzzy matching
    key_terms = {
        "kounhany": ["kounhany", "kounhani", "kounhqny", "kounhqni", "counhany", "kunhany", "koonhany", "kounheny"],
        "voyant": ["voyant", "voyan", "voyent", "voiant"],
        "moteur": ["moteur", "motor", "motur"],
        "frein": ["frein", "fren", "freins", "frins"],
        "huile": ["huile", "huil", "uile"],
        "vidange": ["vidange", "vidence", "videnge"],
        "pneu": ["pneu", "pneus", "peu"],
        "batterie": ["batterie", "bateri", "baterie"],
        "quoi": ["quoi", "qoi", "koi", "aoi"],
        "savez": ["savez", "saver", "sver"],
    }

    words = text.split()
    corrected_words = []

    for word in words:
        word_lower = word.lower().strip(".,!?;:")
        best_match = word  # Default: keep original

        # Check each key term
        for correct_term, variations in key_terms.items():
            # Use fuzzy matching with threshold of 75
            match_result = process.extractOne(word_lower, variations, scorer=fuzz.ratio)
            if match_result and match_result[1] >= 75:  # 75% similarity
                best_match = correct_term
                break

        corrected_words.append(best_match)

    return " ".join(corrected_words)

def is_automobile_related(text: str, user_id: str = None) -> bool:
    """Check if the text is related to automobiles or general conversation"""
    text_lower = text.lower()

    # Always allow general conversation
    if any(keyword in text_lower for keyword in GENERAL_CONVERSATION_KEYWORDS):
        return True

    # Check for automobile keywords
    if any(keyword in text_lower for keyword in AUTOMOBILE_KEYWORDS):
        return True

    # Allow questions (containing question words)
    question_words = ["?", "quoi", "comment", "pourquoi", "quand", "où", "qui", "quel", "quelle", "quels", "quelles"]
    if any(word in text_lower for word in question_words):
        return True

    # Allow short messages (greetings, etc.)
    if len(text.split()) <= 4:
        return True

    # Allow if user has active conversation (context-aware)
    if user_id and user_id in conversation_memory and len(conversation_memory[user_id]) > 0:
        return True

    return False

def process_image_with_yolov8(image_data: str) -> dict:
    """
    Process base64 image with YOLOv8 model and return simple detection results
    """
    try:
        # Decode base64 image
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to OpenCV format
        image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        
        # Run YOLOv8 inference
        results = yolo_model(image_cv)
        
        # Process results - simplified
        detections = []
        detected_classes = set()
        
        for result in results:
            boxes = result.boxes
            if boxes is not None:
                for box in boxes:
                    confidence = float(box.conf[0])
                    class_id = int(box.cls[0])
                    class_name = yolo_model.names[class_id]
                    
                    # Only add if confidence > 0.3 and not duplicate
                    if confidence > 0.3 and class_name not in detected_classes:
                        detected_classes.add(class_name)
                        detections.append({
                            "class": class_name,
                            "confidence": round(confidence, 3)
                        })
        
        return {
            "detections": detections,
            "total_detections": len(detections),
            "detected_classes": list(detected_classes),
            "success": True
        }
        
    except Exception as e:
        return {
            "detections": [],
            "total_detections": 0,
            "detected_classes": [],
            "success": False,
            "error": str(e)
        }

def generate_image_response(detection_results: dict) -> str:
    """
    Generate simple French response for image detection
    """
    if not detection_results["success"]:
        return "❌ Désolé, je n'ai pas pu analyser l'image. Veuillez réessayer avec une image plus claire du tableau de bord."
    
    detections = detection_results["detections"]
    total = detection_results["total_detections"]
    
    if total == 0:
        return "🔍 Aucun indicateur détecté. L'image peut être floue, mal éclairée, ou montrer un tableau de bord éteint."
    
    # Simple response with detected classes
    response_parts = []
    response_parts.append("🚗 **INDICATEURS DÉTECTÉS DANS L'IMAGE:**")
    
    for detection in detections:
        response_parts.append(f"• {detection['class']} ({detection['confidence']:.1%})")
    
    response_parts.append("")
    response_parts.append("💡 *Pour plus d'informations sur un indicateur spécifique, posez-moi une question en texte.*")
    
    return "\n".join(response_parts)

# --- Models ---
class Media(BaseModel):
    format: str
    data: str

class EnhancedData(BaseModel):
    text: Optional[str] = None
    media: Optional[Media] = None

class EnhancedMessage(BaseModel):
    user_id: str
    content_type: str
    timestamp: str
    data: EnhancedData

# --- Endpoints ---
@app.get("/")
async def root():
    return {"message": "API is running", "status": "healthy"}

@app.post("/chat")
async def chat(message: EnhancedMessage):
    try:
        data = message.data
        detected_type = None
        user_id = message.user_id

        # Auto-detect content type
        if data.media and data.media.data:
            media_format = data.media.format.lower()
            if media_format in ["png", "jpg", "jpeg", "gif", "bmp"]:
                detected_type = "image"
            elif media_format in ["mp3", "wav", "ogg", "flac", "m4a"]:
                detected_type = "audio"
            else:
                detected_type = "unknown"
        elif data.text:
            detected_type = "text"
        else:
            return {
                "status": "error",
                "code": 400,
                "message": "No valid text or media data provided.",
                "data": {},
                "timestamp": datetime.utcnow().isoformat()
            }

        # Handle text with conversation memory
        if detected_type == "text":
            start_time = time.time()
            user_prompt = data.text.strip()

            # Apply typo correction
            user_prompt = correct_typos(user_prompt)

            if not user_prompt:
                return {
                    "status": "error",
                    "code": 400,
                    "message": "Empty text input.",
                    "data": {},
                    "timestamp": datetime.utcnow().isoformat()
                }

            # ========== NEW FEATURE 1: OBD CODE DETECTION ==========
            obd_code = detect_obd_code(user_prompt)
            if obd_code:
                obd_info = get_obd_code_info(obd_code)
                if obd_info:
                    response_text = format_obd_response(obd_code, obd_info)
                    response_time = int((time.time() - start_time) * 1000)

                    # Store to conversation memory (FIX: was missing!)
                    conversation_memory[user_id].append({
                        "role": "user",
                        "content": user_prompt,
                        "timestamp": datetime.now()
                    })
                    conversation_memory[user_id].append({
                        "role": "assistant",
                        "content": response_text,
                        "timestamp": datetime.now()
                    })
                    if len(conversation_memory[user_id]) > 10:
                        conversation_memory[user_id] = conversation_memory[user_id][-10:]

                    # Log to analytics
                    log_conversation(
                        user_id=user_id,
                        user_message=user_prompt,
                        ai_response=response_text,
                        response_time_ms=response_time,
                        detected_intent='obd_code',
                        obd_code=obd_code
                    )

                    return {
                        "status": "success",
                        "code": 200,
                        "message": "OBD code processed successfully.",
                        "data": {
                            "response_text": response_text,
                            "obd_code": obd_code,
                            "obd_data": obd_info
                        },
                        "timestamp": datetime.utcnow().isoformat()
                    }
                else:
                    # Code not in database, but recognized format
                    response_text = f"🔧 **Code OBD-II: {obd_code}**\n\nCe code n'est pas dans ma base de données. Je vous recommande de consulter un mécanicien ou d'utiliser KOUNHANY pour trouver un garage audité qui pourra effectuer un diagnostic complet."

                    # Store to conversation memory (FIX: was missing!)
                    conversation_memory[user_id].append({
                        "role": "user",
                        "content": user_prompt,
                        "timestamp": datetime.now()
                    })
                    conversation_memory[user_id].append({
                        "role": "assistant",
                        "content": response_text,
                        "timestamp": datetime.now()
                    })
                    if len(conversation_memory[user_id]) > 10:
                        conversation_memory[user_id] = conversation_memory[user_id][-10:]

                    log_conversation(
                        user_id=user_id,
                        user_message=user_prompt,
                        ai_response=response_text,
                        response_time_ms=int((time.time() - start_time) * 1000),
                        detected_intent='obd_code',
                        obd_code=obd_code
                    )

                    return {
                        "status": "success",
                        "code": 200,
                        "message": "OBD code not found in database.",
                        "data": {"response_text": response_text, "obd_code": obd_code},
                        "timestamp": datetime.utcnow().isoformat()
                    }

            # Check if question is automobile-related or general conversation
            if not is_automobile_related(user_prompt, user_id):
                return {
                    "status": "success",
                    "code": 200,
                    "message": "Text processed successfully.",
                    "data": {
                        "response_text": "🚫 Désolé, je suis spécialisé uniquement dans les questions automobiles. Posez-moi des questions sur les voitures, l'entretien, les voyants du tableau de bord, ou les réparations."
                    },
                    "timestamp": datetime.utcnow().isoformat()
                }

            # ========== NEW FEATURE 2: CHECK LEARNED Q&A ==========
            similar_qa = find_similar_question(user_prompt)
            learned_answer = None
            if similar_qa and similar_qa.get('times_used', 0) >= 3 and similar_qa.get('rating', 0) >= 4.0:
                # Use learned answer if it's been used multiple times with good rating
                learned_answer = similar_qa.get('answer')

            # Get conversation history for this user
            conversation_history = conversation_memory.get(user_id, [])

            # Handle "repeat" or "explain again" requests specifically
            repeat_words = ["répète", "repeat", "encore", "redire", "expliquer le", "explique le",
                           "explain it", "re-explain", "reexplain", "expliquer ça", "explique ça"]
            if any(word in user_prompt.lower() for word in repeat_words):
                if conversation_history:
                    # Get the last assistant response
                    last_responses = [msg for msg in conversation_history if msg["role"] == "assistant"]
                    if last_responses:
                        last_response = last_responses[-1]["content"]
                        # If asking to explain, add context
                        if "expliqu" in user_prompt.lower() or "explain" in user_prompt.lower():
                            response_text = f"Voici l'explication de ma dernière réponse:\n\n{last_response}"
                        else:
                            response_text = last_response

                        # Store and return immediately
                        conversation_memory[user_id].append({
                            "role": "user",
                            "content": user_prompt,
                            "timestamp": datetime.now()
                        })
                        conversation_memory[user_id].append({
                            "role": "assistant",
                            "content": response_text,
                            "timestamp": datetime.now()
                        })

                        return {
                            "status": "success",
                            "code": 200,
                            "message": "Repeat/explain request processed.",
                            "data": {"response_text": response_text},
                            "timestamp": datetime.utcnow().isoformat()
                        }
                    else:
                        response_text = "Je n'ai pas de réponse précédente à répéter."
                else:
                    response_text = "Je n'ai pas de réponse précédente à répéter."

            # Build context from recent conversation (last 4 exchanges)
            context_messages = conversation_history[-4:]
            
            # Build the prompt with conversation history
            context_text = ""
            for msg in context_messages:
                if msg["role"] == "user":
                    context_text += f"Utilisateur: {msg['content']}\n"
                else:
                    context_text += f"Assistant: {msg['content']}\n"

            # Optimized prompt for Qwen2.5-32B using native chat format
            system_prompt = """Tu es un assistant automobile français expert et amical pour KOUNHANY.

=== À PROPOS DE KOUNHANY ===
KOUNHANY est une application marocaine d'après-vente automobile offrant transparence et sécurité.

🚗 3 SERVICES PRINCIPAUX:
1. Forfaits Réparation (Particuliers) - Forfaits avec garages audités et pièces certifiées
2. Vente de Pièces Auto (Garagistes) - Pièces certifiées avec livraison
3. Dépannage & Assistance Routière 24/7 - Géolocalisation en temps réel

🔑 ATOUTS CLÉS:
• Forfaits intelligents et pièces certifiées
• Garages audités et notés par clients
• Carnet d'entretien numérique
• Assistance routière géolocalisée 24/7
• Paiement sécurisé via CMI (aucune donnée bancaire stockée)

📱 FONCTIONNALITÉS:
• Identification véhicule par VIN ou manuellement (Marque > Modèle > Version)
• Comparatif garages: tarifs, proximité, audits, avis clients
• Prise de rendez-vous avec choix date/heure
• Code promo et acompte flexible (30% ou 100%)
• Suivi commandes dans onglet "Réservations"

📧 CONTACT KOUNHANY:
• Email: contactkounhany@gmail.com

RÈGLES IMPORTANTES:
- Quand on te pose des questions sur Kounhany, utilise ces informations
- Réponds de manière concise et claire
- Si l'utilisateur dit "repeat", "répète" ou "je n'ai pas compris", reformule plus simplement
- Pour les salutations, réponds brièvement: "Bonjour ! Comment puis-je vous aider ?"
- Ne jamais inventer de prix ou informations non vérifiées
- Reste concentré sur l'automobile et Kounhany
- INTERDIT: Ne JAMAIS inventer de numéros de téléphone, adresses ou coordonnées
- Si on te demande un numéro de téléphone Kounhany, dis: "Pour le numéro de téléphone, veuillez consulter l'application ou envoyer un email à contactkounhany@gmail.com"
- Termine toujours tes phrases complètement"""

            # Build Qwen2.5 native chat format
            messages_formatted = f"<|im_start|>system\n{system_prompt}<|im_end|>\n"

            # Add conversation history
            for msg in context_messages:
                if msg["role"] == "user":
                    messages_formatted += f"<|im_start|>user\n{msg['content']}<|im_end|>\n"
                else:
                    messages_formatted += f"<|im_start|>assistant\n{msg['content']}<|im_end|>\n"

            # Add current question
            messages_formatted += f"<|im_start|>user\n{user_prompt}<|im_end|>\n<|im_start|>assistant\n"

            response = model(
                messages_formatted,
                max_tokens=400,  # Increased to avoid truncation
                temperature=0.3,
                top_p=0.9,
                repeat_penalty=1.15,
                stop=["<|im_end|>", "<|im_start|>", "Utilisateur:", "Assistant:", "\n\nUtilisateur", "\n\nQuestion"]
            )
            response_text = response["choices"][0]["text"].strip()

            # Aggressive cleaning of leaked prompts and patterns
            cleanup_patterns = [
                "Je n'ai pas compris.",
                "Je n'ai pas compris",
                "Utilisateur:",
                "Assistant:",
                "Question:",
                "Réponse:",
                "<|im_start|>",
                "<|im_end|>",
                "RÈGLES",
                "(Note:",
                "\n\nUtilisateur",
                "\n\nAssistant"
            ]

            for pattern in cleanup_patterns:
                if pattern in response_text:
                    response_text = response_text.split(pattern)[0].strip()

            # Ensure response ends with proper punctuation
            if response_text and not response_text.endswith(('.', '?', '!', ':')):
                # Try to find the last complete sentence
                last_period = max(response_text.rfind('.'), response_text.rfind('!'), response_text.rfind('?'))
                if last_period > len(response_text) * 0.5:  # If we have at least half the response
                    response_text = response_text[:last_period + 1]
                else:
                    response_text = response_text + "."

            # ========== NEW FEATURE 3: WEB SEARCH (if needed) ==========
            search_intent = detect_search_intent(user_prompt)
            web_search_result = None
            user_prompt_lower = user_prompt.lower()

            # Detect if user is asking for news/latest info
            news_keywords = ['actualité', 'actualite', 'news', 'nouveauté', 'nouveau', 'dernière', 'derniere',
                           'latest', 'récent', 'recent', '2024', '2025', 'sortie', 'lancement']
            wants_news = any(kw in user_prompt_lower for kw in news_keywords)

            # Detect if asking about specific car brand news
            car_brands_for_search = ['dacia', 'renault', 'peugeot', 'citroen', 'bmw', 'mercedes', 'audi',
                                    'volkswagen', 'toyota', 'ford', 'fiat', 'tesla', 'hyundai', 'kia']
            mentioned_brand = None
            for brand in car_brands_for_search:
                if brand in user_prompt_lower:
                    mentioned_brand = brand
                    break

            # Perform web search for news queries or price queries
            if search_intent or (wants_news and mentioned_brand):
                try:
                    if wants_news and mentioned_brand:
                        # Search for car brand info (use English for better DuckDuckGo results)
                        search_query = f"{mentioned_brand} car"
                        results = search_duckduckgo(search_query, num_results=3)
                        if results:
                            web_search_result = format_search_results(results)
                            # Prepend a note about the brand
                            if web_search_result:
                                web_search_result = f"📰 **Informations sur {mentioned_brand.title()}:**\n" + web_search_result
                    elif search_intent:
                        web_search_result = perform_search(search_intent)

                    if web_search_result and len(web_search_result) > 50:
                        response_text += "\n\n" + web_search_result
                except Exception as e:
                    print(f"Web search error: {e}")

            # Store conversation in memory
            conversation_memory[user_id].append({
                "role": "user",
                "content": user_prompt,
                "timestamp": datetime.now()
            })
            conversation_memory[user_id].append({
                "role": "assistant",
                "content": response_text,
                "timestamp": datetime.now()
            })

            # Limit conversation history to last 10 messages per user
            if len(conversation_memory[user_id]) > 10:
                conversation_memory[user_id] = conversation_memory[user_id][-10:]

            # ========== NEW FEATURE 4: LOG TO ANALYTICS ==========
            response_time = int((time.time() - start_time) * 1000)
            detected_intent_type = detect_intent(user_prompt)

            log_conversation(
                user_id=user_id,
                user_message=user_prompt,
                ai_response=response_text,
                response_time_ms=response_time,
                detected_intent=detected_intent_type
            )

            # Learn from this conversation (store for future reference)
            if len(response_text) > 50:  # Only learn from substantial responses
                learn_from_conversation(user_prompt, response_text, detected_intent_type)

            return {
                "status": "success",
                "code": 200,
                "message": "Text processed successfully.",
                "data": {
                    "response_text": response_text,
                    "response_time_ms": response_time,
                    "web_search_used": web_search_result is not None
                },
                "timestamp": datetime.utcnow().isoformat()
            }

        # Handle image - simplified processing
        elif detected_type == "image":
            # Process image with YOLOv8
            detection_results = process_image_with_yolov8(data.media.data)

            # Generate simple response
            response_text = generate_image_response(detection_results)

            # Store image detection in conversation memory so user can ask follow-up questions
            detected_indicators = detection_results.get("detected_classes", [])
            if detected_indicators:
                # Create a summary for memory
                indicators_list = ", ".join(detected_indicators)
                memory_text = f"[L'utilisateur a envoyé une photo de tableau de bord. Voyants détectés: {indicators_list}]"

                conversation_memory[user_id].append({
                    "role": "user",
                    "content": memory_text,
                    "timestamp": datetime.now()
                })
                conversation_memory[user_id].append({
                    "role": "assistant",
                    "content": f"J'ai détecté les voyants suivants sur votre tableau de bord: {indicators_list}. Vous pouvez me demander des explications sur chacun de ces voyants.",
                    "timestamp": datetime.now()
                })

                # Limit conversation history
                if len(conversation_memory[user_id]) > 10:
                    conversation_memory[user_id] = conversation_memory[user_id][-10:]

            return {
                "status": "success",
                "code": 200,
                "message": "Image processed successfully.",
                "data": {
                    "response_text": response_text,
                    "detection_data": {
                        "detections": detection_results["detections"],
                        "total": detection_results["total_detections"]
                    }
                },
                "timestamp": datetime.utcnow().isoformat()
            }

        # Handle audio
        elif detected_type == "audio":
            return {
                "status": "success",
                "code": 200,
                "message": f"{detected_type.capitalize()} received successfully.",
                "data": {
                    "response_text": f"J'ai reçu votre audio en format {data.media.format}. L'analyse audio sera disponible prochainement."
                },
                "timestamp": datetime.utcnow().isoformat()
            }

        # Unknown type
        else:
            return {
                "status": "error",
                "code": 400,
                "message": "Unsupported or unknown media format.",
                "data": {},
                "timestamp": datetime.utcnow().isoformat()
            }

    except Exception as e:
        return {
            "status": "error",
            "code": 500,
            "message": str(e),
            "data": {},
            "timestamp": datetime.utcnow().isoformat()
        }

# Health check endpoint
@app.get("/health")
async def health_check():
    try:
        # Test YOLO model
        test_image = np.random.randint(0, 255, (640, 640, 3), dtype=np.uint8)
        results = yolo_model(test_image)
        
        return {
            "status": "healthy",
            "yolo_model_loaded": True,
            "yolo_classes": len(yolo_model.names),
            "llama_model_loaded": True,
            "conversation_memory_users": len(conversation_memory),
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "unhealthy",
            "yolo_model_loaded": False,
            "llama_model_loaded": True,
            "error": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

# Clear conversation endpoint
@app.delete("/conversation/{user_id}")
async def clear_conversation(user_id: str):
    if user_id in conversation_memory:
        del conversation_memory[user_id]
    return {"status": "success", "message": f"Conversation cleared for user {user_id}"}

# --- HTML test page ---
@app.get("/chat-page", response_class=HTMLResponse)
async def chat_page(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

# ========== NEW ENDPOINTS: ANALYTICS & OBD ==========

@app.get("/analytics")
async def get_analytics():
    """Get comprehensive analytics summary."""
    try:
        summary = get_analytics_summary()
        return {
            "status": "success",
            "data": summary,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

@app.get("/analytics/top-questions")
async def get_top_questions_endpoint(limit: int = 20):
    """Get the most frequently asked questions."""
    try:
        questions = get_top_questions(limit)
        return {
            "status": "success",
            "data": questions,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }

@app.get("/obd/{code}")
async def lookup_obd_code(code: str):
    """Look up an OBD-II code."""
    code_upper = code.upper()
    info = get_obd_code_info(code_upper)

    if info:
        return {
            "status": "success",
            "code": code_upper,
            "data": info,
            "formatted_response": format_obd_response(code_upper, info),
            "timestamp": datetime.utcnow().isoformat()
        }
    else:
        return {
            "status": "not_found",
            "code": code_upper,
            "message": f"Code {code_upper} not found in database",
            "timestamp": datetime.utcnow().isoformat()
        }

@app.get("/obd/search/{query}")
async def search_obd_codes_endpoint(query: str):
    """Search OBD codes by keyword."""
    results = search_obd_codes(query)

    return {
        "status": "success",
        "query": query,
        "results": [{"code": code, "description": info["fr"]} for code, info in results],
        "count": len(results),
        "timestamp": datetime.utcnow().isoformat()
    }

@app.get("/search")
async def web_search_endpoint(q: str):
    """Perform a web search for automotive information."""
    try:
        results = search_duckduckgo(q, num_results=5)
        formatted = format_search_results(results) if results else "Aucun résultat trouvé."

        return {
            "status": "success",
            "query": q,
            "results": results,
            "formatted": formatted,
            "timestamp": datetime.utcnow().isoformat()
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "timestamp": datetime.utcnow().isoformat()
        }