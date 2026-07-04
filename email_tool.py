import smtplib
import os
from email.mime.text import MIMEText
from crewai.tools import BaseTool


class SendEmailTool(BaseTool):
    name: str = "send_email"
    description: str = (
        "Sends an email. Requires a recipient email address, a subject line, "
        "and the body text of the email."
    )

    def _run(self, recipient: str, subject: str, body: str) -> str:
        sender = os.getenv("EMAIL_ADDRESS")
        password = os.getenv("EMAIL_APP_PASSWORD")

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(sender, password)
                server.sendmail(sender, recipient, msg.as_string())
            return f"Email successfully sent to {recipient}."
        except Exception as e:
            return f"Failed to send email: {str(e)}"