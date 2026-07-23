from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AboutAccordionForm, AboutSectionForm
from .models import AboutAccordion, AboutSection


def _edit_forms(panels, override_pk=None, override_form=None):
    forms = {}
    for panel in panels:
        if override_pk == panel.pk and override_form is not None:
            forms[panel.pk] = override_form
        else:
            forms[panel.pk] = AboutAccordionForm(
                instance=panel,
                prefix=f'edit-{panel.pk}',
            )
    return forms


def _admin_context(section_form=None, create_form=None, edit_forms=None, open_modal=None):
    panels = AboutAccordion.objects.all()
    section = AboutSection.load()
    return {
        'section': section,
        'section_form': section_form or AboutSectionForm(instance=section),
        'panels': panels,
        'create_form': create_form or AboutAccordionForm(prefix='create'),
        'edit_forms': edit_forms if edit_forms is not None else _edit_forms(panels),
        'open_modal': open_modal,
    }


@login_required
def admin_about(request):
    return render(request, 'backend/about/index.html', _admin_context())


@login_required
def admin_section_update(request):
    section = AboutSection.load()
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutSectionForm(request.POST, request.FILES, instance=section)
    if form.is_valid():
        form.save()
        messages.success(request, 'Section À propos mise à jour.')
        return redirect('about:admin_list')

    messages.error(request, 'Erreur lors de la mise à jour de la section.')
    return render(request, 'backend/about/index.html', _admin_context(section_form=form))


@login_required
def admin_accordion_create(request):
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutAccordionForm(request.POST, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, 'Panneau ajouté avec succès.')
        return redirect('about:admin_list')

    messages.error(request, "Erreur lors de l'ajout du panneau.")
    panels = AboutAccordion.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        create_form=form,
        edit_forms=_edit_forms(panels),
        open_modal='add-panel-modal',
    ))


@login_required
def admin_accordion_update(request, pk):
    panel = get_object_or_404(AboutAccordion, pk=pk)
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutAccordionForm(
        request.POST,
        instance=panel,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Panneau modifié avec succès.')
        return redirect('about:admin_list')

    messages.error(request, 'Erreur lors de la modification du panneau.')
    panels = AboutAccordion.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        edit_forms=_edit_forms(panels, override_pk=pk, override_form=form),
        open_modal=f'edit-panel-modal-{pk}',
    ))


@login_required
def admin_accordion_delete(request, pk):
    if request.method == 'POST':
        panel = get_object_or_404(AboutAccordion, pk=pk)
        panel.delete()
        messages.success(request, 'Panneau supprimé avec succès.')
    return redirect('about:admin_list')
