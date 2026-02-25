import os
from flask import Flask

def create_app():
    base_dir = os.path.dirname(os.path.abspath(__file__))

    templates_path = os.path.join(base_dir, "templates")
    app = Flask(__name__, template_folder=templates_path)

    # forms is now inside app/
    upload_folder = os.path.join(base_dir, "forms", "uploaded")

    # Ensure folder exists
    os.makedirs(upload_folder, exist_ok=True)

    app.config["UPLOAD_FOLDER"] = upload_folder

    from .routes import main
    app.register_blueprint(main)

    return app
