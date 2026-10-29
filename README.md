# 🤖 Local AI Agent

Локальный AI-агент на базе **Strands** и **Ollama**, который умеет проверять доступность серверов по ICMP (ping). Общается через HTTP API (Flask).

## ✨ Возможности
- Проверка статуса сервера (онлайн/офлайн) через встроенный инструмент `get_server_status`.
- Работает полностью локально (без внешних API и ключей).
- Поддержка Markdown в ответах.
- Легкое расширение новыми инструментами (tools).

## 🛠 Стек
- [Ollama](https://ollama.com/) (LLM)
- [Strands Agents](https://github.com/strands-agents/sdk-python) (фреймворк для агентов)
- Flask (HTTP-сервер)

## 🚀 Быстрый старт

### 1. Требования
- Python 3.10+
- Установленный и запущенный [Ollama](https://ollama.com/)

### 2. Установка
```bash
# Клонируйте репозиторий и перейдите в папку
cd Agent

# Создайте виртуальное окружение и активируйте его
python -m venv .venv
source .venv/bin/activate  # Для Linux/macOS
# .venv\Scripts\activate   # Для Windows

# Установите зависимости
pip install -r requirements.txt
