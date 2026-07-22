from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PartenaireForm
from .models import Partenaire


def _edit_forms(partenaires, override_pk=None, override_form=None):
    forms = {}
    for partenaire in partenaires:
        if override_pk == partenaire.pk and override_form is not None:
            forms[partenaire.pk] = override_form
        else:
            forms[partenaire.pk] = PartenaireForm(
                instance=partenaire,
                prefix=f'edit-{partenaire.pk}',
            )
    return forms


@login_required
def admin_partenaire_list(request):
    partenaires = Partenaire.objects.all()
    return render(request, 'backend/partenaire/index.html', {
        'partenaires': partenaires,
        'create_form': PartenaireForm(prefix='create'),
        'edit_forms': _edit_forms(partenaires),
    })


@login_required
def admin_partenaire_create(request):
    partenaires = Partenaire.objects.all()
    if request.method != 'POST':
        return redirect('partenaire:admin_list')

    form = PartenaireForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, 'Partenaire ajouté avec succès.')
        return redirect('partenaire:admin_list')

    messages.error(request, "Erreur lors de l'ajout du partenaire.")
    return render(request, 'backend/partenaire/index.html', {
        'partenaires': partenaires,
        'create_form': form,
        'edit_forms': _edit_forms(partenaires),
        'open_modal': 'add-partenaire-modal',
    })


@login_required
def admin_partenaire_update(request, pk):
    partenaire = get_object_or_404(Partenaire, pk=pk)
    partenaires = Partenaire.objects.all()

    if request.method != 'POST':
        return redirect('partenaire:admin_list')

    form = PartenaireForm(
        request.POST,
        request.FILES,
        instance=partenaire,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Partenaire modifié avec succès.')
        return redirect('partenaire:admin_list')

    messages.error(request, 'Erreur lors de la modification du partenaire.')
    return render(request, 'backend/partenaire/index.html', {
        'partenaires': partenaires,
        'create_form': PartenaireForm(prefix='create'),
        'edit_forms': _edit_forms(partenaires, override_pk=pk, override_form=form),
        'open_modal': f'edit-partenaire-modal-{pk}',
    })


@login_required
def admin_partenaire_delete(request, pk):
    if request.method == 'POST':
        partenaire = get_object_or_404(Partenaire, pk=pk)
        partenaire.delete()
        messages.success(request, 'Partenaire supprimé avec succès.')
    return redirect('partenaire:admin_list')
