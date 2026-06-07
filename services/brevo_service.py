import requests
from services.config import get_env_var


class BrevoService:

    def __init__(self):
        # load API key via centralized config loader
        self.api_key = get_env_var("BREVO_API_KEY")

    def send_email(
        self,
        recipient_email,
        recipient_name,
        subject,
        message
    ):

        url = "https://api.brevo.com/v3/smtp/email"

        headers = {
            "accept": "application/json",
            "api-key": self.api_key,
            "content-type": "application/json"
        }

        payload = {
            "sender": {
                "name": "Kaif Jamadar",
                "email": "kaifjamadar7622@gmail.com"
            },
            "to": [
                {
                    "email": recipient_email,
                    "name": recipient_name
                }
            ],
            "subject": subject,
            "htmlContent": message
        }

        response = requests.post(
            url,
            json=payload,
            headers=headers
        )

        return response.json()