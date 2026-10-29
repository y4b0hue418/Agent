from flask import Flask

from config import FLASK_HOST, FLASK_PORT
from routes import api_bp


def create_app() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(api_bp)
    return app


app = create_app()


if __name__ == "__main__":
    print("Agent started")
    app.run(host=FLASK_HOST, port=FLASK_PORT)
    print("Agent shutdown")