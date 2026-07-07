import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()


def send_alert(subject, body):

    email_address = os.getenv("EMAIL_ADDRESS")
    app_password = os.getenv("EMAIL_APP_PASSWORD")
    alert_email = os.getenv("ALERT_EMAIL")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = alert_email

    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as server:

            server.login(
                email_address,
                app_password
            )

            server.send_message(msg)

        print("Email sent")

    except Exception as e:
        print("Email error:", e)
