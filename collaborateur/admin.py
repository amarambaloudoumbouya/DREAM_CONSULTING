from django.contrib import admin

from .models import Collaborateur


@admin.register(Collaborateur)
class CollaborateurAdmin(admin.ModelAdmin):
    list_display = ('titre', 'sous_titre', 'ordre', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('titre', 'sous_titre')
    list_editable = ('ordre', 'is_active')
    readonly_fields = ('slug', 'created_at', 'updated_at')
