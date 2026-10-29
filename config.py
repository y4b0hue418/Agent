import os

OLLAMA_HOST_URL = os.getenv("OLLAMA_HOST_URL", "http://127.0.0.1:11434")
OLLAMA_MODEL_ID = os.getenv("OLLAMA_MODEL_ID", "qwen3.5:4b")

FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 8080))

# Контекст, подставляемый в system prompt
DISTRO = os.getenv("DISTRO", "Linux")
DE = os.getenv("DE", "unknown")
DATETIME = os.getenv("DATETIME", "")
WINDOWCLASS = os.getenv("WINDOWCLASS", "")