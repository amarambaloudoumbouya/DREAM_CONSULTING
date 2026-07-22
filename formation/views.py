from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render

from .emails import send_inscription_confirmation
from .forms import FormationForm, InscriptionForm
from .models import Formation, Inscription


def formation_list(request):
    formations = Formation.objects.filter(is_active=True)
    return render(request, 'pages/formation.html', {'formations': formations})


def inscription_formation(request):
    selected_slug = request.GET.get('formation', '')
    form = InscriptionForm(
        request.POST or None,
        selected_slug=selected_slug if request.method != 'POST' else None,
    )

    if request.method == 'POST':
        if form.is_valid():
            inscription = form.save()
            try:
                send_inscription_confirmation(inscription)
                messages.success(
                    request,
                    "Votre inscription a bien été envoyée. Un email de confirmation vous a été adressé.",
                )
            except Exception:
                messages.success(
                    request,
                    "Votre inscription a bien été enregistrée. "
                    "L'email de confirmation n'a pas pu être envoyé pour le moment ; nous vous recontacterons rapidement.",
                )
            return redirect('formation:inscription')
        messages.error(request, "Veuillez corriger les erreurs du formulaire.")

    return render(request, 'pages/inscription_formation.html', {
        'form': form,
        'formations': Formation.objects.filter(is_active=True),
        'selected_formation': selected_slug,
    })


def _edit_forms(formations, override_pk=None, override_form=None):
    forms = {}
    for formation in formations:
        if override_pk == formation.pk and override_form is not None:
            forms[formation.pk] = override_form
        else:
            forms[formation.pk] = FormationForm(instance=formation, prefix=f'edit-{formation.pk}')
    return forms


@login_required
def admin_formation_list(request):
    formations = Formation.objects.all()
    return render(request, 'backend/formation/index.html', {
        'formations': formations,
        'create_form': FormationForm(prefix='create'),
        'edit_forms': _edit_forms(formations),
    })


@login_required
def admin_formation_create(request):
    formations = Formation.objects.all()
    if request.method != 'POST':
        return redirect('formation:admin_list')

    form = FormationForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, 'Formation ajoutée avec succès.')
        return redirect('formation:admin_list')

    messages.error(request, "Erreur lors de l'ajout de la formation.")
    return render(request, 'backend/formation/index.html', {
        'formations': formations,
        'create_form': form,
        'edit_forms': _edit_forms(formations),
        'open_modal': 'add-formation-modal',
    })


@login_required
def admin_formation_update(request, pk):
    formation = get_object_or_404(Formation, pk=pk)
    formations = Formation.objects.all()

    if request.method != 'POST':
        return redirect('formation:admin_list')

    form = FormationForm(
        request.POST,
        request.FILES,
        instance=formation,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Formation modifiée avec succès.')
        return redirect('formation:admin_list')

    messages.error(request, 'Erreur lors de la modification de la formation.')
    return render(request, 'backend/formation/index.html', {
        'formations': formations,
        'create_form': FormationForm(prefix='create'),
        'edit_forms': _edit_forms(formations, override_pk=pk, override_form=form),
        'open_modal': f'edit-formation-modal-{pk}',
    })


@login_required
def admin_formation_delete(request, pk):
    if request.method == 'POST':
        formation = get_object_or_404(Formation, pk=pk)
        formation.delete()
        messages.success(request, 'Formation supprimée avec succès.')
    return redirect('formation:admin_list')


@login_required
def admin_inscription_list(request):
    formation_id = request.GET.get('formation')
    statut = request.GET.get('statut')

    inscriptions = Inscription.objects.prefetch_related('formations').all()
    if formation_id:
        inscriptions = inscriptions.filter(formations__pk=formation_id)
    if statut:
        inscriptions = inscriptions.filter(statut=statut)

    formations_stats = Formation.objects.annotate(
        nb_inscrits=Count('inscriptions', distinct=True),
    ).order_by('ordre', 'titre')

    total_inscrits = Inscription.objects.count()
    total_nouvelles = Inscription.objects.filter(statut='nouvelle').count()
    total_confirmees = Inscription.objects.filter(statut='confirmee').count()
    total_refusees = Inscription.objects.filter(statut='refusee').count()

    def pct(value):
        if not total_inscrits:
            return 0
        return round((value / total_inscrits) * 100)

    context = {
        'inscriptions': inscriptions.distinct(),
        'total_inscrits': total_inscrits,
        'total_nouvelles': total_nouvelles,
        'total_confirmees': total_confirmees,
        'total_refusees': total_refusees,
        'pct_nouvelles': pct(total_nouvelles),
        'pct_confirmees': pct(total_confirmees),
        'pct_refusees': pct(total_refusees),
        'formations_stats': formations_stats,
        'selected_formation': formation_id,
        'selected_statut': statut,
        'statut_choices': Inscription.STATUT_CHOICES,
    }
    return render(request, 'backend/formation/inscriptions.html', context)


@login_required
def admin_inscription_update_statut(request, pk):
    if request.method == 'POST':
        inscription = get_object_or_404(Inscription, pk=pk)
        nouveau_statut = request.POST.get('statut')
        if nouveau_statut in dict(Inscription.STATUT_CHOICES):
            inscription.statut = nouveau_statut
            inscription.save(update_fields=['statut', 'updated_at'])
            messages.success(request, f'Statut de {inscription.prenom} {inscription.nom} mis à jour.')
    return redirect('formation:admin_inscriptions')
