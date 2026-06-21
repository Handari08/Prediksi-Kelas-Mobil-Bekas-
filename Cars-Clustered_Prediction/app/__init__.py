from flask import Flask
from flask_cors import CORS
from app.routes import main
import os

def create_app():
    # ✅ kasih tahu lokasi templates
    app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), "..", "templates"))

    CORS(app)

    app.register_blueprint(main)

    return app