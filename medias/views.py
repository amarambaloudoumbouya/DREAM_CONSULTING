from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BrandingForm, PhotographieForm, VideoForm
from .models import Branding, Photographie, Video


def _edit_forms(items, form_class, override_pk=None, override_form=None):
    forms = {}
    for item in items:
        if override_pk == item.pk and override_form is not None:
            forms[item.pk] = override_form
        else:
            forms[item.pk] = form_class(instance=item, prefix=f'edit-{item.pk}')
    return forms


def _make_crud(model, form_class, template_name, url_namespace, label):
    list_name = f'{url_namespace}_list'
    context_map = {
        'photographie': 'photographies',
        'branding': 'brandings',
        'video': 'videos',
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


(
    admin_photographie_list,
    admin_photographie_create,
    admin_photographie_update,
    admin_photographie_delete,
) = _make_crud(
    Photographie,
    PhotographieForm,
    'backend/medias/photographie.html',
    'photographie',
    'Photographie',
)

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
