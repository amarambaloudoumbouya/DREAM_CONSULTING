from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    AboutAccordionForm,
    AboutCounterForm,
    AboutSectionForm,
    AboutTimelineForm,
)
from .models import AboutAccordion, AboutCounter, AboutSection, AboutTimeline


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


def _edit_counter_forms(counters, override_pk=None, override_form=None):
    forms = {}
    for counter in counters:
        if override_pk == counter.pk and override_form is not None:
            forms[counter.pk] = override_form
        else:
            forms[counter.pk] = AboutCounterForm(
                instance=counter,
                prefix=f'edit-counter-{counter.pk}',
            )
    return forms


def _edit_timeline_forms(items, override_pk=None, override_form=None):
    forms = {}
    for item in items:
        if override_pk == item.pk and override_form is not None:
            forms[item.pk] = override_form
        else:
            forms[item.pk] = AboutTimelineForm(
                instance=item,
                prefix=f'edit-timeline-{item.pk}',
            )
    return forms


def _admin_context(
    section_form=None,
    create_form=None,
    edit_forms=None,
    counter_create_form=None,
    counter_edit_forms=None,
    timeline_create_form=None,
    timeline_edit_forms=None,
    open_modal=None,
):
    panels = AboutAccordion.objects.all()
    counters = AboutCounter.objects.all()
    timelines = AboutTimeline.objects.all()
    section = AboutSection.load()
    return {
        'section': section,
        'section_form': section_form or AboutSectionForm(instance=section),
        'panels': panels,
        'create_form': create_form or AboutAccordionForm(prefix='create'),
        'edit_forms': edit_forms if edit_forms is not None else _edit_forms(panels),
        'counters': counters,
        'counter_create_form': counter_create_form or AboutCounterForm(prefix='create-counter'),
        'counter_edit_forms': (
            counter_edit_forms
            if counter_edit_forms is not None
            else _edit_counter_forms(counters)
        ),
        'timelines': timelines,
        'timeline_create_form': (
            timeline_create_form or AboutTimelineForm(prefix='create-timeline')
        ),
        'timeline_edit_forms': (
            timeline_edit_forms
            if timeline_edit_forms is not None
            else _edit_timeline_forms(timelines)
        ),
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


@login_required
def admin_counter_create(request):
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutCounterForm(request.POST, prefix='create-counter')
    if form.is_valid():
        form.save()
        messages.success(request, 'Compteur ajouté avec succès.')
        return redirect('about:admin_list')

    messages.error(request, "Erreur lors de l'ajout du compteur.")
    counters = AboutCounter.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        counter_create_form=form,
        counter_edit_forms=_edit_counter_forms(counters),
        open_modal='add-counter-modal',
    ))


@login_required
def admin_counter_update(request, pk):
    counter = get_object_or_404(AboutCounter, pk=pk)
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutCounterForm(
        request.POST,
        instance=counter,
        prefix=f'edit-counter-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Compteur modifié avec succès.')
        return redirect('about:admin_list')

    messages.error(request, 'Erreur lors de la modification du compteur.')
    counters = AboutCounter.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        counter_edit_forms=_edit_counter_forms(
            counters,
            override_pk=pk,
            override_form=form,
        ),
        open_modal=f'edit-counter-modal-{pk}',
    ))


@login_required
def admin_counter_delete(request, pk):
    if request.method == 'POST':
        counter = get_object_or_404(AboutCounter, pk=pk)
        counter.delete()
        messages.success(request, 'Compteur supprimé avec succès.')
    return redirect('about:admin_list')


@login_required
def admin_timeline_create(request):
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutTimelineForm(request.POST, request.FILES, prefix='create-timeline')
    if form.is_valid():
        form.save()
        messages.success(request, 'Étape timeline ajoutée avec succès.')
        return redirect('about:admin_list')

    messages.error(request, "Erreur lors de l'ajout de l'étape.")
    timelines = AboutTimeline.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        timeline_create_form=form,
        timeline_edit_forms=_edit_timeline_forms(timelines),
        open_modal='add-timeline-modal',
    ))


@login_required
def admin_timeline_update(request, pk):
    item = get_object_or_404(AboutTimeline, pk=pk)
    if request.method != 'POST':
        return redirect('about:admin_list')

    form = AboutTimelineForm(
        request.POST,
        request.FILES,
        instance=item,
        prefix=f'edit-timeline-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Étape timeline modifiée avec succès.')
        return redirect('about:admin_list')

    messages.error(request, "Erreur lors de la modification de l'étape.")
    timelines = AboutTimeline.objects.all()
    return render(request, 'backend/about/index.html', _admin_context(
        timeline_edit_forms=_edit_timeline_forms(
            timelines,
            override_pk=pk,
            override_form=form,
        ),
        open_modal=f'edit-timeline-modal-{pk}',
    ))


@login_required
def admin_timeline_delete(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(AboutTimeline, pk=pk)
        item.delete()
        messages.success(request, 'Étape timeline supprimée avec succès.')
    return redirect('about:admin_list')
