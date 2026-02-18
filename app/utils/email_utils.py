import smtplib
import os
import traceback
import atexit
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv("EMAIL_USER")
EMAIL_APP_PASSWORD = os.getenv("EMAIL_PASS")

email_server = None


def start_email_server():
    global email_server
    try:
        email_server = smtplib.SMTP("smtp.gmail.com", 587)
        email_server.starttls()
        email_server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        print("✅ Email server started and authenticated.")
    except Exception as e:
        print(f"❌ Failed to start email server: {e}")
        traceback.print_exc()
        email_server = None


def close_email_server():
    global email_server
    if email_server:
        email_server.quit()
        print("📪 Email server connection closed.")


atexit.register(close_email_server)


def send_email_with_attachment(subject, body, to, attachment_path):
    if not email_server:
        print("❌ Email server is not initialized.")
        return

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with open(attachment_path, "rb") as f:
        part = MIMEApplication(
            f.read(),
            Name=os.path.basename(attachment_path),
        )
        part["Content-Disposition"] = (
            f'attachment; filename="{os.path.basename(attachment_path)}"'
        )
        msg.attach(part)

    try:
        email_server.send_message(msg)
        print("✅ Email sent successfully.")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
