from agent import my_agent

PROMPTS = [
    "Проверь, в сети ли 127.0.0.1",
    "Жив ли google.com?",
    "Пингни 10.255.255.1 — отвечает?",
    "Привет! Кто ты?",  # контроль: инструмент НЕ должен вызываться
]

def ask(prompt: str) -> str:
    r = my_agent(prompt)
    return r.message.get("content", [{}])[0].get("text", str(r))

if __name__ == "__main__":
    for p in PROMPTS:
        print(f"\n=== {p} ===")
        try:
            print(ask(p))
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")