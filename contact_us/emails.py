from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_contact_confirmation(message_contact):
    subject = 'Confirmation de votre message — Dream Consulting Com'
    context = {
        'message_contact': message_contact,
        'site_name': 'Dream Consulting Com',
    }
    text_body = render_to_string('contact_us/emails/confirmation.txt', context)
    html_body = render_to_string('contact_us/emails/confirmation.html', context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[message_contact.email],
    )
    email.attach_alternative(html_body, 'text/html')
    email.send(fail_silently=False)


def send_contact_reponse(message_contact):
    subject = f'Réponse à votre message — {message_contact.sujet}'
    context = {
        'message_contact': message_contact,
        'site_name': 'Dream Consulting Com',
    }
    text_body = render_to_string('contact_us/emails/reponse.txt', context)
    html_body = render_to_string('contact_us/emails/reponse.html', context)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[message_contact.email],
    )
    email.attach_alternative(html_body, 'text/html')
    email.send(fail_silently=False)
