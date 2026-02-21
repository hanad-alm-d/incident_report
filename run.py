from app import create_app
from app.utils.email_utils import start_email_server, email_server_instance
import threading
import os

app = create_app()

# Start email server in a thread, singleton ensures only one connection
if email_server_instance() is None:
    thread = threading.Thread(target=start_email_server)
    thread.daemon = True
    thread.start()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000, threaded=True)