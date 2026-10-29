from flask import Blueprint, request, jsonify

from agent import my_agent

api_bp = Blueprint("api", __name__)


@api_bp.route("/", methods=["GET"])
def health():
    return "AI Agent is running!"


@api_bp.route("/", methods=["POST"])
def invoke():
    payload = request.get_json(silent=True) or {}
    prompt = payload.get("prompt", "Hello!")

    result = my_agent(prompt)
    return jsonify({
        "response": result.message.get("content", [{}])[0].get("text", str(result))
    })