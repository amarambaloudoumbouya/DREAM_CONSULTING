from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_demande_confirmation(demande):
    subject = 'Confirmation de votre demande de devis — Dream Consulting Com'
    context = {
        'demande': demande,
        'prestations': demande.get_prestations_display(),
        'site_name': 'Dream Consulting Com',
    }
    text_body = render_to_string('devis/emails/demande_confirmation.txt', context)
    html_body = render_to_string('devis/emails/demande_confirmation.html', context)

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[demande.email],
    )
    message.attach_alternative(html_body, 'text/html')
    message.send(fail_silently=False)


def send_demande_retour(demande):
    subject = 'Retour sur votre demande de devis — Dream Consulting Com'
    context = {
        'demande': demande,
        'prestations': demande.get_prestations_display(),
        'site_name': 'Dream Consulting Com',
    }
    text_body = render_to_string('devis/emails/demande_retour.txt', context)
    html_body = render_to_string('devis/emails/demande_retour.html', context)

    message = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[demande.email],
    )
    message.attach_alternative(html_body, 'text/html')
    message.send(fail_silently=False)
