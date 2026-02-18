from app import create_app
from app.utils.email_utils import start_email_server

app = create_app()

if __name__ == "__main__":
    start_email_server()
    app.run(debug=True, host="0.0.0.0")
