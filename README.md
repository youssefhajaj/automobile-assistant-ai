<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/CUDA-12.0+-76B900?style=for-the-badge&logo=nvidia&logoColor=white" alt="CUDA">
  <img src="https://img.shields.io/badge/LLM-Qwen2.5--32B-FF6F00?style=for-the-badge" alt="LLM">
  <img src="https://img.shields.io/badge/YOLOv8-Computer%20Vision-00FFFF?style=for-the-badge" alt="YOLOv8">
</p>

<h1 align="center">🚗 Automobile Assistant AI</h1>

<p align="center">
  <strong>An intelligent French-language automobile technical assistant powered by state-of-the-art AI</strong>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-architecture">Architecture</a> •
  <a href="#-requirements">Requirements</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-api-reference">API Reference</a> •
  <a href="#-usage">Usage</a>
</p>

---

## 🌟 Overview

**Automobile Assistant AI** is a production-ready FastAPI application designed for the **KOUNHANY** platform - a Moroccan automotive aftermarket service. It combines a powerful 32-billion parameter language model with computer vision capabilities to provide:

- 💬 **Intelligent Conversations** - Natural French-language dialogue about automotive topics
- 🔍 **Dashboard Detection** - AI-powered recognition of 68 different dashboard warning indicators
- 🔧 **OBD-II Diagnostics** - Instant lookup of 500+ diagnostic trouble codes
- 📊 **Analytics & Learning** - Continuous improvement through conversation analysis
- 🌐 **Web Search Integration** - Real-time information retrieval for current data

---

## ✨ Features

### 🤖 Large Language Model
- **Model**: Qwen2.5-32B-Instruct (Q5_K_M quantization)
- **Parameters**: 32 Billion
- **Context Window**: 4,096 tokens
- **Specialization**: French automotive technical assistance
- **Anti-hallucination**: Strict prompting to prevent fabricated information

### 👁️ Computer Vision
- **Model**: YOLOv8 Custom-trained
- **Classes**: 68 dashboard warning indicators
- **Accuracy**: High-confidence detection (>30% threshold)
- **Input**: Base64-encoded images (JPG, PNG)

### 🔧 OBD-II Database
- **Coverage**: 500+ diagnostic codes
- **Categories**: P (Powertrain), B (Body), C (Chassis), U (Network)
- **Information**: French descriptions, severity levels, causes, solutions
- **Response Time**: <100ms (instant lookup)

### 📝 Smart Features
- **Typo Correction**: Fuzzy matching for misspelled words (like ChatGPT)
- **Conversation Memory**: Per-user context retention (last 4 exchanges)
- **Intent Detection**: Automatic categorization of queries
- **Response Cleaning**: Removes system prompt leaks and artifacts

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Request                          │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
                ┌───────────────────────┐
                │   FastAPI Endpoint    │
                │      /chat (POST)     │
                └───────────┬───────────┘
                            │
            ┌───────────────┴───────────────┐
            │                               │
            ▼                               ▼
    ┌──────────────┐              ┌──────────────────┐
    │  Text Input  │              │   Image Input    │
    └──────┬───────┘              └────────┬─────────┘
           │                               │
           ▼                               ▼
    ┌──────────────────┐          ┌────────────────────┐
    │  Typo Correction │          │  YOLOv8 Detection  │
    │  (RapidFuzz)     │          │  (68 Classes)      │
    └──────┬───────────┘          └────────┬───────────┘
           │                               │
           ▼                               │
    ┌──────────────────┐                   │
    │  OBD Code Check  │                   │
    │  (500+ Codes)    │                   │
    └──────┬───────────┘                   │
           │                               │
           ▼                               │
    ┌─────────────────────────┐           │
    │ Conversation Memory     │           │
    │ (Per User Context)      │           │
    └──────┬──────────────────┘           │
           │                               │
           ▼                               │
    ┌─────────────────────────┐           │
    │   Qwen2.5-32B-Instruct  │           │
    │   • GPU: RTX 4090       │           │
    │   • VRAM: 23GB/24GB     │           │
    └──────┬──────────────────┘           │
           │                               │
           └───────────────┬───────────────┘
                           │
                           ▼
                ┌──────────────────────┐
                │    JSON Response     │
                └──────────────────────┘
```

---

## 💻 Requirements

### Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **GPU** | RTX 3090 (24GB) | **RTX 4090 (24GB)** |
| **VRAM** | 24GB | 24GB |
| **RAM** | 32GB | 64GB |
| **Storage** | 50GB SSD | 100GB NVMe SSD |
| **CPU** | 8 cores | 16+ cores |

> ⚠️ **Important**: This project requires a **24GB VRAM GPU** (RTX 3090/4090 or equivalent). The Qwen2.5-32B model uses approximately **23GB VRAM** during inference.

### Software Requirements

- **OS**: Ubuntu 20.04+ / Debian 11+
- **Python**: 3.10+
- **CUDA**: 12.0+
- **cuDNN**: 8.0+
- **Driver**: NVIDIA 525.0+

---

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/youssefhajaj/automobile-assistant-ai.git
cd automobile-assistant-ai
```

### Step 2: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate  # Windows

# Upgrade pip
pip install --upgrade pip
```

### Step 3: Install Dependencies

```bash
# Core dependencies
pip install fastapi uvicorn pydantic pillow numpy jinja2

# Machine Learning
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu121
pip install ultralytics opencv-python

# LLM with CUDA support
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu121

# Additional features
pip install rapidfuzz python-docx
```

### Step 4: Download the LLM Model

```bash
# Install huggingface-cli if not already installed
pip install huggingface_hub

# Login to HuggingFace (optional, for gated models)
huggingface-cli login

# Download Qwen2.5-32B-Instruct (Q5_K_M quantization - 22GB)
huggingface-cli download Qwen/Qwen2.5-32B-Instruct-GGUF \
    qwen2.5-32b-instruct-q5_k_m.gguf \
    --local-dir . \
    --local-dir-use-symlinks False

# Rename to expected filename
mv qwen2.5-32b-instruct-q5_k_m.gguf Qwen2.5-32B-Instruct-Q5_K_M.gguf
```

### Step 5: Configure GPU (CUDA)

```bash
# Verify CUDA installation
nvidia-smi

# Expected output should show:
# - Driver Version: 525.0+
# - CUDA Version: 12.0+
# - GPU: RTX 4090 or equivalent with 24GB VRAM

# Test PyTorch CUDA
python -c "import torch; print(f'CUDA available: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0)}')"
```

### Step 6: Start the Server

```bash
# Development mode
uvicorn api_server:app --host 0.0.0.0 --port 8000 --reload

# Production mode (background)
nohup uvicorn api_server:app --host 0.0.0.0 --port 8000 > api.log 2>&1 &

# Check logs
tail -f api.log
```

### Step 7: Verify Installation

```bash
# Health check
curl http://localhost:8000/

# Expected response:
# {"message":"API is running","status":"healthy"}

# Detailed health check
curl http://localhost:8000/health
```

---

## 📡 API Reference

### Base URL
```
http://your-server-ip:8000
```

### Endpoints

#### `GET /` - Health Check
```bash
curl http://localhost:8000/
```
**Response:**
```json
{
  "message": "API is running",
  "status": "healthy"
}
```

---

#### `POST /chat` - Main Chat Endpoint

**Text Request:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "unique_user_id",
    "content_type": "text",
    "timestamp": "2025-01-01T12:00:00.000000Z",
    "data": {
      "text": "Bonjour, comment changer l'\''huile moteur?"
    }
  }'
```

**Text Response:**
```json
{
  "status": "success",
  "code": 200,
  "message": "Text processed successfully.",
  "data": {
    "response_text": "Bonjour ! Pour changer l'huile moteur, voici les étapes..."
  },
  "timestamp": "2025-01-01T12:00:05.123456"
}
```

**Image Request:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "unique_user_id",
    "content_type": "image",
    "timestamp": "2025-01-01T12:00:00.000000Z",
    "data": {
      "media": {
        "format": "jpg",
        "data": "BASE64_ENCODED_IMAGE_STRING"
      }
    }
  }'
```

**Image Response:**
```json
{
  "status": "success",
  "code": 200,
  "message": "Image processed successfully.",
  "data": {
    "response_text": "🚗 **INDICATEURS DÉTECTÉS:**\n• check_engine (95.2%)\n• oil_pressure (87.3%)",
    "detection_data": {
      "detections": [
        {"class": "check_engine", "confidence": 0.952},
        {"class": "oil_pressure", "confidence": 0.873}
      ],
      "total": 2
    }
  }
}
```

---

#### `GET /obd/{code}` - OBD-II Code Lookup

```bash
curl http://localhost:8000/obd/P0420
```

**Response:**
```json
{
  "code": "P0420",
  "description_en": "Catalyst System Efficiency Below Threshold (Bank 1)",
  "description_fr": "Efficacité du catalyseur en dessous du seuil (Banc 1)",
  "severity": "medium",
  "cause": "Catalyseur usé ou défectueux, sonde lambda défaillante",
  "solution": "Vérifier les sondes lambda, remplacer le catalyseur si nécessaire"
}
```

---

#### `GET /chat-page` - Web Interface

Access the built-in chat interface at:
```
http://localhost:8000/chat-page
```

---

#### `GET /analytics` - Usage Analytics

```bash
curl http://localhost:8000/analytics
```

---

#### `DELETE /conversation/{user_id}` - Clear Conversation History

```bash
curl -X DELETE http://localhost:8000/conversation/user123
```

---

## 🎯 Usage

### Web Interface

1. Navigate to `http://your-server:8000/chat-page`
2. Type your question in French
3. Click send or press Enter
4. For dashboard images, click the camera icon to upload

### Mobile Integration

```python
import requests

# Text query
response = requests.post(
    "http://your-server:8000/chat",
    json={
        "user_id": "mobile_user_123",
        "content_type": "text",
        "timestamp": "2025-01-01T12:00:00.000000Z",
        "data": {"text": "Que signifie le voyant moteur?"}
    }
)
print(response.json())
```

### OBD-II Quick Lookup

```bash
# In chat, just type the code:
"P0420"
"Mon code erreur est C0035"
"J'ai eu le code U0100"
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `MODEL_PATH` | Path to GGUF model | `./Qwen2.5-32B-Instruct-Q5_K_M.gguf` |
| `YOLO_MODEL` | Path to YOLOv8 model | `./best.pt` |
| `N_GPU_LAYERS` | GPU layers (-1 = all) | `-1` |
| `N_CTX` | Context window size | `4096` |
| `PORT` | Server port | `8000` |

### Model Parameters (in `api_server.py`)

```python
model = Llama(
    model_path="Qwen2.5-32B-Instruct-Q5_K_M.gguf",
    n_gpu_layers=-1,      # All layers on GPU
    n_ctx=4096,           # Context window
    n_batch=256,          # Batch size
    n_threads=32,         # CPU threads
    n_threads_batch=32,
    verbose=False
)
```

### Inference Parameters

```python
response = model(
    prompt,
    max_tokens=200,       # Maximum response length
    temperature=0.3,      # Lower = more focused
    top_p=0.9,
    repeat_penalty=1.15,
    stop=["<|im_end|>", "<|im_start|>"]
)
```

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| **Text Response Time** | 2-4 seconds |
| **Image Detection Time** | 1-2 seconds |
| **OBD Code Lookup** | <100ms |
| **GPU Memory Usage** | 23GB / 24GB |
| **Concurrent Users** | 10-20 (recommended) |

---

## 🗂️ Project Structure

```
automobile-assistant-ai/
├── api_server.py          # Main FastAPI application
├── keywords.py            # French automotive keywords
├── obd_codes.py           # OBD-II diagnostic codes database
├── analytics.py           # Analytics & learning system
├── web_search.py          # DuckDuckGo integration
├── best.pt                # YOLOv8 model (68 classes)
├── templates/
│   └── chat.html          # Web interface
├── .gitignore
└── README.md
```

---

## 🛡️ Security Notes

- Never commit API keys or tokens to the repository
- Use environment variables for sensitive configuration
- The analytics database contains user conversations - handle appropriately
- Implement rate limiting for production deployments

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## 📄 License

This project is proprietary software developed for KOUNHANY.

---

## 👨‍💻 Author

**Youssef Hajaj**

---

<p align="center">
  <strong>Built with ❤️ for the Moroccan automotive community</strong>
</p>
