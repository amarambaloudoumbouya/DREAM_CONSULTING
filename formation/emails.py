from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_inscription_confirmation(inscription):
    """Envoie un email de confirmation au client après inscription."""
    subject = 'Confirmation de votre inscription — Dream Consulting Com'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [inscription.email]

    context = {
        'inscription': inscription,
        'formations': inscription.formations.all(),
        'site_name': 'Dream Consulting Com',
    }

    text_body = render_to_string('formation/emails/inscription_confirmation.txt', context)
    html_body = render_to_string('formation/emails/inscription_confirmation.html', context)

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=from_email,
        to=to_email,
    )
    message.attach_alternative(html_body, 'text/html')
    message.send(fail_silently=False)
