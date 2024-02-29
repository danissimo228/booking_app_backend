from config.settings import SENDER_EMAIL, EMAIL_PASSWORD, SMTP_SERVER, SMTP_PORT
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(token: str, email_to: str) -> None:
    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = email_to
    msg['Subject'] = 'Password recovery'

    # Add the message body
    message = f'Your token: {token}'
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        server.sendmail(SENDER_EMAIL, email_to, msg.as_string())
