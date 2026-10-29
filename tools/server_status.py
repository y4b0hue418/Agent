import os
import platform
from strands import tool


@tool
def get_server_status(server_name: str):
    """
    Check the current status of a server.
    Args:
        server_name: The name or ip of the server to check.
    """
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    response = os.system(f"ping {param} 1 {server_name}")
    if response == 0:
        return f"Сервер '{server_name}' онлайн!"
    return f"Сервер '{server_name}' офлайн!"