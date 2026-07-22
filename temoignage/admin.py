from django.contrib import admin

from .models import Temoignage


@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'fonction', 'note', 'statut', 'created_at', 'publie_at')
    list_filter = ('statut', 'note', 'created_at')
    search_fields = ('nom', 'prenom', 'email', 'avis')
    readonly_fields = ('slug', 'created_at', 'updated_at', 'publie_at')
