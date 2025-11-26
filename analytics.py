# analytics.py - Analytics and Learning System for Kounhany AI
# Logs conversations, tracks patterns, and learns from successful interactions

import sqlite3
import json
from datetime import datetime, timedelta
from collections import Counter
from typing import Optional, List, Dict, Tuple
import re
import os

DATABASE_PATH = "/workspace/ai/kounhany_analytics.db"

def get_db_connection():
    """Get database connection with proper settings."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize the analytics database with all required tables."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Table for all conversations
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            user_message TEXT NOT NULL,
            ai_response TEXT NOT NULL,
            response_time_ms INTEGER,
            content_type TEXT DEFAULT 'text',
            detected_intent TEXT,
            obd_code_detected TEXT,
            was_helpful INTEGER DEFAULT NULL,
            feedback TEXT
        )
    ''')

    # Table for learned Q&A pairs (successful interactions)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS learned_qa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_pattern TEXT NOT NULL,
            best_answer TEXT NOT NULL,
            category TEXT,
            times_used INTEGER DEFAULT 1,
            avg_rating REAL DEFAULT 5.0,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(question_pattern)
        )
    ''')

    # Table for common questions analytics
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS question_analytics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_normalized TEXT NOT NULL UNIQUE,
            count INTEGER DEFAULT 1,
            last_asked DATETIME DEFAULT CURRENT_TIMESTAMP,
            category TEXT
        )
    ''')

    # Table for user sessions
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            session_start DATETIME DEFAULT CURRENT_TIMESTAMP,
            session_end DATETIME,
            message_count INTEGER DEFAULT 0,
            topics_discussed TEXT
        )
    ''')

    # Table for daily stats
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_stats (
            date DATE PRIMARY KEY,
            total_messages INTEGER DEFAULT 0,
            unique_users INTEGER DEFAULT 0,
            obd_queries INTEGER DEFAULT 0,
            kounhany_queries INTEGER DEFAULT 0,
            technical_queries INTEGER DEFAULT 0,
            avg_response_time_ms REAL
        )
    ''')

    # Table for search results cache (for internet search)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS search_cache (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query TEXT NOT NULL,
            results TEXT NOT NULL,
            cached_at DATETIME DEFAULT CURRENT_TIMESTAMP,
            expires_at DATETIME
        )
    ''')

    conn.commit()
    conn.close()
    print("✅ Analytics database initialized successfully")

def log_conversation(
    user_id: str,
    user_message: str,
    ai_response: str,
    response_time_ms: int = 0,
    content_type: str = "text",
    detected_intent: str = None,
    obd_code: str = None
):
    """Log a conversation to the database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Detect intent if not provided
    if not detected_intent:
        detected_intent = detect_intent(user_message)

    cursor.execute('''
        INSERT INTO conversations
        (user_id, user_message, ai_response, response_time_ms, content_type, detected_intent, obd_code_detected)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, user_message, ai_response, response_time_ms, content_type, detected_intent, obd_code))

    # Update question analytics
    normalized = normalize_question(user_message)
    cursor.execute('''
        INSERT INTO question_analytics (question_normalized, category, count, last_asked)
        VALUES (?, ?, 1, CURRENT_TIMESTAMP)
        ON CONFLICT(question_normalized) DO UPDATE SET
            count = count + 1,
            last_asked = CURRENT_TIMESTAMP
    ''', (normalized, detected_intent))

    # Update daily stats
    today = datetime.now().strftime('%Y-%m-%d')
    cursor.execute('''
        INSERT INTO daily_stats (date, total_messages, unique_users, obd_queries, kounhany_queries, technical_queries)
        VALUES (?, 1, 1, ?, ?, ?)
        ON CONFLICT(date) DO UPDATE SET
            total_messages = total_messages + 1,
            obd_queries = obd_queries + ?,
            kounhany_queries = kounhany_queries + ?,
            technical_queries = technical_queries + ?
    ''', (
        today,
        1 if obd_code else 0,
        1 if detected_intent == 'kounhany' else 0,
        1 if detected_intent == 'technical' else 0,
        1 if obd_code else 0,
        1 if detected_intent == 'kounhany' else 0,
        1 if detected_intent == 'technical' else 0
    ))

    conn.commit()
    conn.close()

def detect_intent(message: str) -> str:
    """Detect the intent of a user message."""
    message_lower = message.lower()

    # OBD code detection
    if re.search(r'[pPbBcCuU][0-9]{4}', message):
        return 'obd_code'

    # Kounhany related
    kounhany_keywords = ['kounhany', 'application', 'réserver', 'garage', 'forfait', 'service']
    if any(kw in message_lower for kw in kounhany_keywords):
        return 'kounhany'

    # Technical questions
    technical_keywords = ['huile', 'moteur', 'frein', 'pneu', 'vidange', 'batterie', 'voyant',
                         'entretien', 'réparation', 'panne', 'bruit', 'problème']
    if any(kw in message_lower for kw in technical_keywords):
        return 'technical'

    # Greetings
    greetings = ['bonjour', 'salut', 'hello', 'bonsoir', 'hey', 'coucou']
    if any(kw in message_lower for kw in greetings):
        return 'greeting'

    return 'general'

def normalize_question(question: str) -> str:
    """Normalize a question for pattern matching."""
    # Remove punctuation and convert to lowercase
    normalized = re.sub(r'[^\w\s]', '', question.lower())
    # Remove extra whitespace
    normalized = ' '.join(normalized.split())
    # Remove common filler words
    stopwords = ['le', 'la', 'les', 'un', 'une', 'des', 'de', 'du', 'et', 'est', 'je', 'tu', 'il', 'elle',
                 'nous', 'vous', 'ils', 'elles', 'mon', 'ma', 'mes', 'ton', 'ta', 'tes', 'son', 'sa', 'ses']
    words = [w for w in normalized.split() if w not in stopwords]
    return ' '.join(words)

def learn_from_conversation(question: str, answer: str, category: str = None, rating: float = 5.0):
    """Store a successful Q&A pair for future reference."""
    conn = get_db_connection()
    cursor = conn.cursor()

    pattern = normalize_question(question)

    cursor.execute('''
        INSERT INTO learned_qa (question_pattern, best_answer, category, avg_rating)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(question_pattern) DO UPDATE SET
            best_answer = CASE WHEN ? > avg_rating THEN ? ELSE best_answer END,
            times_used = times_used + 1,
            avg_rating = (avg_rating * times_used + ?) / (times_used + 1),
            updated_at = CURRENT_TIMESTAMP
    ''', (pattern, answer, category, rating, rating, answer, rating))

    conn.commit()
    conn.close()

def find_similar_question(question: str) -> Optional[Dict]:
    """Find a similar question in the learned Q&A database."""
    conn = get_db_connection()
    cursor = conn.cursor()

    pattern = normalize_question(question)
    words = pattern.split()

    if not words:
        return None

    # Search for questions containing similar words
    placeholders = ' OR '.join(['question_pattern LIKE ?' for _ in words])
    like_patterns = [f'%{word}%' for word in words]

    cursor.execute(f'''
        SELECT question_pattern, best_answer, category, times_used, avg_rating
        FROM learned_qa
        WHERE {placeholders}
        ORDER BY times_used DESC, avg_rating DESC
        LIMIT 1
    ''', like_patterns)

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            'question': row['question_pattern'],
            'answer': row['best_answer'],
            'category': row['category'],
            'times_used': row['times_used'],
            'rating': row['avg_rating']
        }
    return None

def get_top_questions(limit: int = 20) -> List[Dict]:
    """Get the most frequently asked questions."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT question_normalized, count, category, last_asked
        FROM question_analytics
        ORDER BY count DESC
        LIMIT ?
    ''', (limit,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_daily_stats(days: int = 7) -> List[Dict]:
    """Get daily statistics for the last N days."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT date, total_messages, unique_users, obd_queries, kounhany_queries, technical_queries
        FROM daily_stats
        ORDER BY date DESC
        LIMIT ?
    ''', (days,))

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]

def get_analytics_summary() -> Dict:
    """Get a comprehensive analytics summary."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Total conversations
    cursor.execute('SELECT COUNT(*) as total FROM conversations')
    total_conversations = cursor.fetchone()['total']

    # Unique users
    cursor.execute('SELECT COUNT(DISTINCT user_id) as users FROM conversations')
    unique_users = cursor.fetchone()['users']

    # Conversations today
    cursor.execute('''
        SELECT COUNT(*) as today
        FROM conversations
        WHERE DATE(timestamp) = DATE('now')
    ''')
    today_conversations = cursor.fetchone()['today']

    # Intent distribution
    cursor.execute('''
        SELECT detected_intent, COUNT(*) as count
        FROM conversations
        WHERE detected_intent IS NOT NULL
        GROUP BY detected_intent
        ORDER BY count DESC
    ''')
    intent_distribution = {row['detected_intent']: row['count'] for row in cursor.fetchall()}

    # Top 10 questions
    cursor.execute('''
        SELECT question_normalized, count
        FROM question_analytics
        ORDER BY count DESC
        LIMIT 10
    ''')
    top_questions = [(row['question_normalized'], row['count']) for row in cursor.fetchall()]

    # Learned Q&A count
    cursor.execute('SELECT COUNT(*) as learned FROM learned_qa')
    learned_qa_count = cursor.fetchone()['learned']

    # OBD codes queried
    cursor.execute('''
        SELECT obd_code_detected, COUNT(*) as count
        FROM conversations
        WHERE obd_code_detected IS NOT NULL
        GROUP BY obd_code_detected
        ORDER BY count DESC
        LIMIT 10
    ''')
    top_obd_codes = [(row['obd_code_detected'], row['count']) for row in cursor.fetchall()]

    conn.close()

    return {
        'total_conversations': total_conversations,
        'unique_users': unique_users,
        'today_conversations': today_conversations,
        'intent_distribution': intent_distribution,
        'top_questions': top_questions,
        'learned_qa_count': learned_qa_count,
        'top_obd_codes': top_obd_codes
    }

def get_unanswered_patterns() -> List[str]:
    """Find questions that the AI struggled to answer (potential knowledge gaps)."""
    conn = get_db_connection()
    cursor = conn.cursor()

    # Find questions with short responses or error patterns
    cursor.execute('''
        SELECT DISTINCT user_message
        FROM conversations
        WHERE LENGTH(ai_response) < 50
        OR ai_response LIKE '%je ne sais pas%'
        OR ai_response LIKE '%je ne peux pas%'
        OR ai_response LIKE '%désolé%'
        ORDER BY timestamp DESC
        LIMIT 20
    ''')

    rows = cursor.fetchall()
    conn.close()

    return [row['user_message'] for row in rows]

# Cache functions for internet search
def cache_search_results(query: str, results: str, expires_hours: int = 24):
    """Cache search results."""
    conn = get_db_connection()
    cursor = conn.cursor()

    expires_at = datetime.now() + timedelta(hours=expires_hours)

    cursor.execute('''
        INSERT OR REPLACE INTO search_cache (query, results, cached_at, expires_at)
        VALUES (?, ?, CURRENT_TIMESTAMP, ?)
    ''', (query.lower(), results, expires_at))

    conn.commit()
    conn.close()

def get_cached_search(query: str) -> Optional[str]:
    """Get cached search results if not expired."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('''
        SELECT results FROM search_cache
        WHERE query = ? AND expires_at > CURRENT_TIMESTAMP
    ''', (query.lower(),))

    row = cursor.fetchone()
    conn.close()

    return row['results'] if row else None

def clean_expired_cache():
    """Remove expired cache entries."""
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM search_cache WHERE expires_at < CURRENT_TIMESTAMP')

    conn.commit()
    conn.close()

# Initialize database on import
init_database()

# Pre-populate with some common Q&A patterns
def seed_learned_qa():
    """Seed the database with common Q&A patterns."""
    common_qa = [
        ("c'est quoi kounhany", "KOUNHANY est une application marocaine d'après-vente automobile offrant des forfaits réparation avec garages audités, vente de pièces certifiées, et assistance routière 24/7.", "kounhany"),
        ("comment réserver réparation", "Pour réserver : 1) Identifiez votre véhicule par VIN ou manuellement, 2) Choisissez le service, 3) Comparez les garages, 4) Prenez rendez-vous, 5) Payez l'acompte (30% ou 100%).", "kounhany"),
        ("quels services kounhany", "KOUNHANY propose 3 services: 1) Forfaits Réparation pour particuliers, 2) Vente de pièces pour garagistes, 3) Dépannage et assistance routière 24/7.", "kounhany"),
        ("voyant moteur allumé", "Le voyant moteur peut indiquer plusieurs problèmes. Un diagnostic OBD est recommandé pour identifier le code d'erreur exact. Avec KOUNHANY, trouvez un garage audité pour un diagnostic précis.", "technical"),
        ("quand changer huile", "En général, changez l'huile tous les 10 000 à 15 000 km ou une fois par an. Consultez le manuel de votre véhicule pour les recommandations spécifiques.", "technical"),
        ("pression pneus recommandée", "La pression recommandée se trouve sur l'étiquette dans la portière conducteur ou dans le manuel. En général: 2.0 à 2.5 bar pour les voitures standard.", "technical"),
        ("batterie faible symptomes", "Symptômes d'une batterie faible: démarrage lent, voyant batterie allumé, phares faibles, équipements électriques défaillants. Faites tester votre batterie.", "technical"),
        ("entretien vidange", "La vidange comprend: remplacement huile moteur, filtre à huile, vérification des niveaux. Recommandé tous les 10 000-15 000 km selon le véhicule.", "technical"),
    ]

    conn = get_db_connection()
    cursor = conn.cursor()

    for question, answer, category in common_qa:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO learned_qa (question_pattern, best_answer, category)
                VALUES (?, ?, ?)
            ''', (question, answer, category))
        except:
            pass

    conn.commit()
    conn.close()

# Seed on first run
seed_learned_qa()
