from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy

from .forms import (
    MembreCreateForm,
    MembreUpdateForm,
    UserCreateForm,
    UserUpdateForm,
)
from .models import CustomerUser


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        if not self.request.POST.get('remember'):
            self.request.session.set_expiry(0)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('accounts:login')


def _edit_forms(users, override_pk=None, override_form=None):
    forms = {}
    for user in users:
        if override_pk == user.pk and override_form is not None:
            forms[user.pk] = override_form
        else:
            forms[user.pk] = UserUpdateForm(instance=user, prefix=f'edit-{user.pk}')
    return forms


def users_list(request):
    users = CustomerUser.objects.all()
    return render(request, 'backend/accounts/index.html', {
        'users': users,
        'create_form': UserCreateForm(prefix='create'),
        'edit_forms': _edit_forms(users),
    })


def user_create(request):
    users = CustomerUser.objects.all()
    if request.method != 'POST':
        return redirect('accounts:users_list')

    form = UserCreateForm(request.POST, request.FILES, prefix='create')
    if form.is_valid():
        form.save()
        messages.success(request, "Utilisateur ajouté avec succès.")
        return redirect('accounts:users_list')

    messages.error(request, "Erreur lors de l'ajout de l'utilisateur.")
    return render(request, 'backend/accounts/index.html', {
        'users': users,
        'create_form': form,
        'edit_forms': _edit_forms(users),
        'open_modal': 'add-user-modal',
    })


def user_update(request, pk):
    user = get_object_or_404(CustomerUser, pk=pk)
    users = CustomerUser.objects.all()

    if request.method != 'POST':
        return redirect('accounts:users_list')

    form = UserUpdateForm(request.POST, request.FILES, instance=user, prefix=f'edit-{pk}')
    if form.is_valid():
        form.save()
        messages.success(request, "Utilisateur modifié avec succès.")
        return redirect('accounts:users_list')

    messages.error(request, "Erreur lors de la modification de l'utilisateur.")
    return render(request, 'backend/accounts/index.html', {
        'users': users,
        'create_form': UserCreateForm(prefix='create'),
        'edit_forms': _edit_forms(users, override_pk=pk, override_form=form),
        'open_modal': f'edit-user-modal-{pk}',
    })


def user_delete(request, pk):
    if request.method == 'POST':
        user = get_object_or_404(CustomerUser, pk=pk)
        user.delete()
        messages.success(request, "Utilisateur supprimé avec succès.")
    return redirect('accounts:users_list')


def _membre_qs():
    return CustomerUser.objects.filter(role='membre')


def _edit_membre_forms(membres, override_pk=None, override_form=None):
    forms = {}
    for membre in membres:
        if override_pk == membre.pk and override_form is not None:
            forms[membre.pk] = override_form
        else:
            forms[membre.pk] = MembreUpdateForm(
                instance=membre,
                prefix=f'edit-membre-{membre.pk}',
            )
    return forms


@login_required
def membres_list(request):
    membres = _membre_qs()
    return render(request, 'backend/accounts/membres.html', {
        'membres': membres,
        'create_form': MembreCreateForm(prefix='create-membre'),
        'edit_forms': _edit_membre_forms(membres),
    })


@login_required
def membre_create(request):
    membres = _membre_qs()
    if request.method != 'POST':
        return redirect('accounts:membres_list')

    form = MembreCreateForm(request.POST, request.FILES, prefix='create-membre')
    if form.is_valid():
        form.save()
        messages.success(request, 'Membre ajouté avec succès.')
        return redirect('accounts:membres_list')

    messages.error(request, "Erreur lors de l'ajout du membre.")
    return render(request, 'backend/accounts/membres.html', {
        'membres': membres,
        'create_form': form,
        'edit_forms': _edit_membre_forms(membres),
        'open_modal': 'add-membre-modal',
    })


@login_required
def membre_update(request, pk):
    membre = get_object_or_404(CustomerUser, pk=pk, role='membre')
    membres = _membre_qs()

    if request.method != 'POST':
        return redirect('accounts:membres_list')

    form = MembreUpdateForm(
        request.POST,
        request.FILES,
        instance=membre,
        prefix=f'edit-membre-{pk}',
    )
    if form.is_valid():
        form.save()
        messages.success(request, 'Membre modifié avec succès.')
        return redirect('accounts:membres_list')

    messages.error(request, 'Erreur lors de la modification du membre.')
    return render(request, 'backend/accounts/membres.html', {
        'membres': membres,
        'create_form': MembreCreateForm(prefix='create-membre'),
        'edit_forms': _edit_membre_forms(membres, override_pk=pk, override_form=form),
        'open_modal': f'edit-membre-modal-{pk}',
    })


@login_required
def membre_delete(request, pk):
    if request.method == 'POST':
        membre = get_object_or_404(CustomerUser, pk=pk, role='membre')
        membre.delete()
        messages.success(request, 'Membre supprimé avec succès.')
    return redirect('accounts:membres_list')
