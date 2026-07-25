from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .emails import send_contact_confirmation, send_contact_reponse
from .forms import MessageContactForm, ReponseContactForm
from .models import MessageContact


def contact_public(request):
    form = MessageContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            message_contact = form.save()
            try:
                send_contact_confirmation(message_contact)
                messages.success(
                    request,
                    "Votre message a bien été envoyé. "
                    "Un email de confirmation vous a été adressé.",
                )
            except Exception:
                messages.success(
                    request,
                    "Votre message a bien été enregistré. "
                    "Nous vous répondrons rapidement.",
                )
            return redirect('site_:contact')
        messages.error(request, 'Veuillez corriger les erreurs du formulaire.')

    return render(request, 'pages/contact.html', {'form': form})


@login_required
def admin_message_list(request):
    statut = request.GET.get('statut')
    messages_qs = MessageContact.objects.all()
    if statut:
        messages_qs = messages_qs.filter(statut=statut)

    total = MessageContact.objects.count()
    total_nouveaux = MessageContact.objects.filter(statut='nouveau').count()
    total_en_cours = MessageContact.objects.filter(statut='en_cours').count()
    total_repondus = MessageContact.objects.filter(statut='repondu').count()
    total_archives = MessageContact.objects.filter(statut='archive').count()

    def pct(value):
        if not total:
            return 0
        return round((value / total) * 100)

    return render(request, 'backend/contact_us/index.html', {
        'messages_contact': messages_qs,
        'total': total,
        'total_nouveaux': total_nouveaux,
        'total_en_cours': total_en_cours,
        'total_repondus': total_repondus,
        'total_archives': total_archives,
        'pct_nouveaux': pct(total_nouveaux),
        'pct_en_cours': pct(total_en_cours),
        'pct_repondus': pct(total_repondus),
        'pct_archives': pct(total_archives),
        'selected_statut': statut,
        'statut_choices': MessageContact.STATUT_CHOICES,
    })


@login_required
def admin_message_reponse(request, pk):
    message_contact = get_object_or_404(MessageContact, pk=pk)

    if request.method != 'POST':
        return redirect('contact_us:admin_list')

    form = ReponseContactForm(request.POST)
    if form.is_valid():
        message_contact.statut = form.cleaned_data['statut']
        message_contact.reponse = form.cleaned_data['reponse']
        envoyer = form.cleaned_data.get('envoyer_email')

        if envoyer:
            try:
                send_contact_reponse(message_contact)
                message_contact.reponse_envoyee_at = timezone.now()
                if message_contact.statut == 'nouveau':
                    message_contact.statut = 'repondu'
                messages.success(
                    request,
                    f'Réponse envoyée à {message_contact.email} et message mis à jour.',
                )
            except Exception:
                messages.warning(
                    request,
                    "Le message a été mis à jour, mais l'email de réponse n'a pas pu être envoyé.",
                )
        else:
            messages.success(request, 'Message mis à jour sans envoi d’email.')

        message_contact.save()
    else:
        messages.error(request, 'Veuillez corriger le formulaire de réponse.')

    return redirect('contact_us:admin_list')


@login_required
def admin_message_delete(request, pk):
    if request.method == 'POST':
        message_contact = get_object_or_404(MessageContact, pk=pk)
        message_contact.delete()
        messages.success(request, 'Message supprimé avec succès.')
    return redirect('contact_us:admin_list')
