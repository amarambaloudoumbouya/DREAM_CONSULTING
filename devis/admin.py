from django.contrib import admin

from .models import DemandeDevis


@admin.register(DemandeDevis)
class DemandeDevisAdmin(admin.ModelAdmin):
    list_display = (
        'nom_complet',
        'email',
        'telephone',
        'type_evenement',
        'date_evenement',
        'statut',
        'created_at',
    )
    list_filter = ('statut', 'type_evenement', 'created_at')
    search_fields = ('nom_complet', 'email', 'telephone', 'lieu')
    readonly_fields = ('created_at', 'updated_at', 'retour_envoye_at')
