from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import SliderForm
from .models import Slider


def _edit_forms(sliders, override_pk=None, override_form=None):
    forms = {}
    for slider in sliders:
        if override_pk == slider.pk and override_form is not None:
            forms[slider.pk] = override_form
        else:
            forms[slider.pk] = SliderForm(
                instance=slider,
                prefix=f'edit-{slider.pk}',
            )
    return forms


@login_required
def admin_slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'backend/slider/index.html', {
        'sliders': sliders,
        'create_form': SliderForm(prefix='create'),
        'edit_forms': _edit_forms(sliders),
    })


@login_required
def admin_slider_create(request):
    sliders = Slider.objects.all()
    if request.method != 'POST':
        return redirect('slider:admin_list')

    form = SliderForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, 'Slider ajouté avec succès.')
        return redirect('slider:admin_list')

    messages.error(request, "Erreur lors de l'ajout du slider.")
    return render(request, 'backend/slider/index.html', {
        'sliders': sliders,
        'create_form': form,
        'edit_forms': _edit_forms(sliders),
        'open_modal': 'add-slider-modal',
    })


@login_required
def admin_slider_update(request, pk):
    slider = get_object_or_404(Slider, pk=pk)
    sliders = Slider.objects.all()

    if request.method != 'POST':
        return redirect('slider:admin_list')

    form = SliderForm(
        request.POST,
        request.FILES,
        instance=slider,
        prefix=f'edit-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Slider modifié avec succès.')
        return redirect('slider:admin_list')

    messages.error(request, 'Erreur lors de la modification du slider.')
    return render(request, 'backend/slider/index.html', {
        'sliders': sliders,
        'create_form': SliderForm(prefix='create'),
        'edit_forms': _edit_forms(sliders, override_pk=pk, override_form=form),
        'open_modal': f'edit-slider-modal-{pk}',
    })


@login_required
def admin_slider_delete(request, pk):
    if request.method == 'POST':
        slider = get_object_or_404(Slider, pk=pk)
        slider.delete()
        messages.success(request, 'Slider supprimé avec succès.')
    return redirect('slider:admin_list')
