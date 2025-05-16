import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Replace with your actual Gmail address and App Password
EMAIL_ADDRESS = "hanadalimohamed1@gmail.com"        # Your Gmail address
EMAIL_APP_PASSWORD = "ggyl dezk tdpp mqgh"      # Your 16-digit App Password

def send_email():
    # Compose the email
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = "hanadalimohamed1@gmail.com"        # Replace with recipient email
    msg['Subject'] = "Test Email from Python via Gmail"

    # Email content
    body = "✅ Hello! This is a test email sent using Gmail SMTP and Python."
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(EMAIL_ADDRESS, EMAIL_APP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("🎉 Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

# Run the email function
if __name__ == "__main__":
    send_email()
