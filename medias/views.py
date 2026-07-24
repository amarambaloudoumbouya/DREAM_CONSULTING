from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    BrandingForm,
    PhotographieCreateForm,
    PhotographieForm,
    VideoForm,
    WebDesignForm,
)
from .models import Branding, Photographie, Video, WebDesign


def _edit_forms(items, form_class, override_pk=None, override_form=None):
    forms = {}
    for item in items:
        if override_pk == item.pk and override_form is not None:
            forms[item.pk] = override_form
        else:
            forms[item.pk] = form_class(instance=item, prefix=f'edit-{item.pk}')
    return forms


def _photo_categories():
    return list(
        Photographie.objects.order_by('categorie')
        .values_list('categorie', flat=True)
        .distinct()
    )


def _photo_admin_context(**overrides):
    items = Photographie.objects.all()
    context = {
        'photographies': items,
        'create_form': PhotographieCreateForm(prefix='create'),
        'edit_forms': _edit_forms(items, PhotographieForm),
        'photo_categories': _photo_categories(),
    }
    context.update(overrides)
    return context


def _make_crud(model, form_class, template_name, url_namespace, label):
    list_name = f'{url_namespace}_list'
    context_map = {
        'branding': 'brandings',
        'video': 'videos',
        'web_design': 'web_designs',
    }
    context_key = context_map[url_namespace]
    modal_prefix = url_namespace

    @login_required
    def admin_list(request):
        items = model.objects.all()
        return render(request, template_name, {
            context_key: items,
            'create_form': form_class(prefix='create'),
            'edit_forms': _edit_forms(items, form_class),
        })

    @login_required
    def admin_create(request):
        items = model.objects.all()
        if request.method != 'POST':
            return redirect(f'medias:{list_name}')

        form = form_class(request.POST, request.FILES, prefix='create')
        if form.is_valid():
            form.save()
            messages.success(request, f'{label} ajouté(e) avec succès.')
            return redirect(f'medias:{list_name}')

        messages.error(request, "Erreur lors de l'ajout.")
        return render(request, template_name, {
            context_key: items,
            'create_form': form,
            'edit_forms': _edit_forms(items, form_class),
            'open_modal': f'add-{modal_prefix}-modal',
        })

    @login_required
    def admin_update(request, pk):
        item = get_object_or_404(model, pk=pk)
        items = model.objects.all()
        if request.method != 'POST':
            return redirect(f'medias:{list_name}')

        form = form_class(
            request.POST,
            request.FILES,
            instance=item,
            prefix=f'edit-{pk}',
        )
        if form.is_valid():
            form.save()
            messages.success(request, f'{label} modifié(e) avec succès.')
            return redirect(f'medias:{list_name}')

        messages.error(request, 'Erreur lors de la modification.')
        return render(request, template_name, {
            context_key: items,
            'create_form': form_class(prefix='create'),
            'edit_forms': _edit_forms(items, form_class, override_pk=pk, override_form=form),
            'open_modal': f'edit-{modal_prefix}-modal-{pk}',
        })

    @login_required
    def admin_delete(request, pk):
        if request.method == 'POST':
            item = get_object_or_404(model, pk=pk)
            item.delete()
            messages.success(request, f'{label} supprimé(e) avec succès.')
        return redirect(f'medias:{list_name}')

    return admin_list, admin_create, admin_update, admin_delete


@login_required
def admin_photographie_list(request):
    return render(request, 'backend/medias/photographie.html', _photo_admin_context())


@login_required
def admin_photographie_create(request):
    if request.method != 'POST':
        return redirect('medias:photographie_list')

    form = PhotographieCreateForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        created = form.save()
        count = len(created)
        if count > 1:
            messages.success(
                request,
                f'{count} photographies ajoutées dans la catégorie « {created[0].categorie} ».',
            )
        else:
            messages.success(request, 'Photographie ajoutée avec succès.')
        return redirect('medias:photographie_list')

    messages.error(request, "Erreur lors de l'ajout.")
    return render(
        request,
        'backend/medias/photographie.html',
        _photo_admin_context(create_form=form, open_modal='add-photographie-modal'),
    )


@login_required
def admin_photographie_update(request, pk):
    item = get_object_or_404(Photographie, pk=pk)
    items = Photographie.objects.all()
    if request.method != 'POST':
        return redirect('medias:photographie_list')

    form = PhotographieForm(
        request.POST,
        request.FILES,
        instance=item,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Photographie modifiée avec succès.')
        return redirect('medias:photographie_list')

    messages.error(request, 'Erreur lors de la modification.')
    return render(
        request,
        'backend/medias/photographie.html',
        _photo_admin_context(
            edit_forms=_edit_forms(items, PhotographieForm, override_pk=pk, override_form=form),
            open_modal=f'edit-photographie-modal-{pk}',
        ),
    )


@login_required
def admin_photographie_delete(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Photographie, pk=pk)
        item.delete()
        messages.success(request, 'Photographie supprimée avec succès.')
    return redirect('medias:photographie_list')


(
    admin_branding_list,
    admin_branding_create,
    admin_branding_update,
    admin_branding_delete,
) = _make_crud(
    Branding,
    BrandingForm,
    'backend/medias/branding.html',
    'branding',
    'Branding',
)

(
    admin_video_list,
    admin_video_create,
    admin_video_update,
    admin_video_delete,
) = _make_crud(
    Video,
    VideoForm,
    'backend/medias/video.html',
    'video',
    'Vidéo',
)

(
    admin_web_design_list,
    admin_web_design_create,
    admin_web_design_update,
    admin_web_design_delete,
) = _make_crud(
    WebDesign,
    WebDesignForm,
    'backend/medias/web_design.html',
    'web_design',
    'Projet web design',
)
