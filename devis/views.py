from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .emails import send_demande_confirmation, send_demande_retour
from .forms import DemandeDevisForm, RetourDevisForm
from .models import DemandeDevis


def demande_devis(request):
    form = DemandeDevisForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            demande = form.save()
            try:
                send_demande_confirmation(demande)
                messages.success(
                    request,
                    "Votre demande de devis a bien été envoyée. "
                    "Un email de confirmation vous a été adressé.",
                )
            except Exception:
                messages.success(
                    request,
                    "Votre demande de devis a bien été enregistrée. "
                    "Nous vous recontacterons rapidement.",
                )
            return redirect('site_:demande_avis')
        messages.error(request, 'Veuillez corriger les erreurs du formulaire.')

    return render(request, 'pages/demande_avis.html', {'form': form})


@login_required
def admin_demande_list(request):
    statut = request.GET.get('statut')
    demandes = DemandeDevis.objects.all()
    if statut:
        demandes = demandes.filter(statut=statut)

    total = DemandeDevis.objects.count()
    total_nouvelles = DemandeDevis.objects.filter(statut='nouvelle').count()
    total_analyse = DemandeDevis.objects.filter(statut='en_analyse').count()
    total_traitees = DemandeDevis.objects.filter(statut='traitee').count()
    total_refusees = DemandeDevis.objects.filter(statut='refusee').count()

    def pct(value):
        if not total:
            return 0
        return round((value / total) * 100)

    return render(request, 'backend/devis/index.html', {
        'demandes': demandes,
        'total': total,
        'total_nouvelles': total_nouvelles,
        'total_analyse': total_analyse,
        'total_traitees': total_traitees,
        'total_refusees': total_refusees,
        'pct_nouvelles': pct(total_nouvelles),
        'pct_analyse': pct(total_analyse),
        'pct_traitees': pct(total_traitees),
        'pct_refusees': pct(total_refusees),
        'selected_statut': statut,
        'statut_choices': DemandeDevis.STATUT_CHOICES,
    })


@login_required
def admin_demande_retour(request, pk):
    demande = get_object_or_404(DemandeDevis, pk=pk)

    if request.method != 'POST':
        return redirect('devis:admin_list')

    form = RetourDevisForm(request.POST)
    if form.is_valid():
        demande.statut = form.cleaned_data['statut']
        demande.retour = form.cleaned_data['retour']
        envoyer = form.cleaned_data.get('envoyer_email')

        if envoyer:
            try:
                send_demande_retour(demande)
                demande.retour_envoye_at = timezone.now()
                messages.success(
                    request,
                    f'Retour envoyé à {demande.email} et demande mise à jour.',
                )
            except Exception:
                messages.warning(
                    request,
                    "La demande a été mise à jour, mais l'email de retour n'a pas pu être envoyé.",
                )
        else:
            messages.success(request, 'Demande mise à jour sans envoi d’email.')

        demande.save()
    else:
        messages.error(request, 'Veuillez corriger le formulaire de retour.')

    return redirect('devis:admin_list')
