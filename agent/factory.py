from strands import Agent
from strands.models.ollama import OllamaModel

from config import OLLAMA_HOST_URL, OLLAMA_MODEL_ID
from tools import get_server_status
from agent.prompts import SYSTEM_PROMPT


def create_agent() -> Agent:
    model = OllamaModel(host=OLLAMA_HOST_URL, model_id=OLLAMA_MODEL_ID)
    return Agent(
        model=model,
        tools=[get_server_status],
        system_prompt=SYSTEM_PROMPT,
    )


my_agent = create_agent()