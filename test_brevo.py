from services.brevo_service import BrevoService

brevo = BrevoService()

result = brevo.send_email(
    recipient_email="kaifjamadar7622@gmail.com",
    recipient_name="Kaif",
    subject="Brevo Test",
    message="""
    <h1>Hello</h1>
    <p>Testing Brevo API Integration</p>
    """
)

print(result)