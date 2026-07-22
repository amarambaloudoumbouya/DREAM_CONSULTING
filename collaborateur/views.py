from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CollaborateurForm
from .models import Collaborateur


def _edit_forms(collaborateurs, override_pk=None, override_form=None):
    forms = {}
    for collaborateur in collaborateurs:
        if override_pk == collaborateur.pk and override_form is not None:
            forms[collaborateur.pk] = override_form
        else:
            forms[collaborateur.pk] = CollaborateurForm(
                instance=collaborateur,
                prefix=f'edit-{collaborateur.pk}',
            )
    return forms


@login_required
def admin_collaborateur_list(request):
    collaborateurs = Collaborateur.objects.all()
    return render(request, 'backend/collaborateur/index.html', {
        'collaborateurs': collaborateurs,
        'create_form': CollaborateurForm(prefix='create'),
        'edit_forms': _edit_forms(collaborateurs),
    })


@login_required
def admin_collaborateur_create(request):
    collaborateurs = Collaborateur.objects.all()
    if request.method != 'POST':
        return redirect('collaborateur:admin_list')

    form = CollaborateurForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, 'Collaborateur ajouté avec succès.')
        return redirect('collaborateur:admin_list')

    messages.error(request, "Erreur lors de l'ajout du collaborateur.")
    return render(request, 'backend/collaborateur/index.html', {
        'collaborateurs': collaborateurs,
        'create_form': form,
        'edit_forms': _edit_forms(collaborateurs),
        'open_modal': 'add-collaborateur-modal',
    })


@login_required
def admin_collaborateur_update(request, pk):
    collaborateur = get_object_or_404(Collaborateur, pk=pk)
    collaborateurs = Collaborateur.objects.all()

    if request.method != 'POST':
        return redirect('collaborateur:admin_list')

    form = CollaborateurForm(
        request.POST,
        request.FILES,
        instance=collaborateur,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Collaborateur modifié avec succès.')
        return redirect('collaborateur:admin_list')

    messages.error(request, 'Erreur lors de la modification du collaborateur.')
    return render(request, 'backend/collaborateur/index.html', {
        'collaborateurs': collaborateurs,
        'create_form': CollaborateurForm(prefix='create'),
        'edit_forms': _edit_forms(collaborateurs, override_pk=pk, override_form=form),
        'open_modal': f'edit-collaborateur-modal-{pk}',
    })


@login_required
def admin_collaborateur_delete(request, pk):
    if request.method == 'POST':
        collaborateur = get_object_or_404(Collaborateur, pk=pk)
        collaborateur.delete()
        messages.success(request, 'Collaborateur supprimé avec succès.')
    return redirect('collaborateur:admin_list')
