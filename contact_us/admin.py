from django.contrib import admin

from .models import MessageContact


@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = (
        'nom_complet',
        'email',
        'telephone',
        'sujet',
        'statut',
        'created_at',
    )
    list_filter = ('statut', 'created_at')
    search_fields = ('nom_complet', 'email', 'telephone', 'sujet', 'message')
    readonly_fields = ('slug', 'created_at', 'updated_at', 'reponse_envoyee_at')
    list_editable = ('statut',)
