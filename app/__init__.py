from flask import Flask
import os

def create_app():
    # __file__ is app/__init__.py
    # ../templates goes up one level to project root, then into templates/
    templates_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../templates")

    app = Flask(__name__, template_folder=templates_path)

    # ===== FOLDER STRUCTURE =====
    FORMS_FOLDER = "forms"
    UPLOAD_FOLDER = os.path.join(FORMS_FOLDER, "uploaded")
    app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

    from .routes import main
    app.register_blueprint(main)

    return app
