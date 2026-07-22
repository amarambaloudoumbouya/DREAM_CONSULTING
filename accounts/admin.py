from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

from .models import CustomerUser


class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ('email', 'prenoms', 'nom', 'tel')


class CustomerUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomerUser
        fields = '__all__'


@admin.register(CustomerUser)
class CustomerUserAdmin(BaseUserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomerUserChangeForm
    change_password_form = AdminPasswordChangeForm

    ordering = ('email',)
    list_display = ('email', 'prenoms', 'nom', 'role', 'tel', 'is_staff', 'is_active', 'created_at')
    list_filter = ('is_staff', 'is_active', 'sexe', 'role')
    search_fields = ('email', 'prenoms', 'nom', 'tel')
    readonly_fields = ('slug', 'created_at', 'updated_at', 'last_login')
    filter_horizontal = ('groups', 'user_permissions')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Informations', {
            'fields': (
                'prenoms',
                'nom',
                'sexe',
                'role',
                'tel',
                'adresse',
                'fonction_poste',
                'photo',
            ),
        }),
        ('Réseaux sociaux', {
            'fields': (
                'reseau_social_facebook',
                'reseau_social_twitter',
                'reseau_social_linkedin',
                'reseau_social_youtube',
            ),
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Métadonnées', {'fields': ('slug', 'last_login', 'created_at', 'updated_at')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'prenoms',
                'nom',
                'tel',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            ),
        }),
    )
