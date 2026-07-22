from django.contrib import admin

from .models import Formation, Inscription


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'duree', 'niveau', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active', 'niveau')
    search_fields = ('titre', 'description')
    prepopulated_fields = {'slug': ('titre',)}
    list_editable = ('ordre', 'is_active')


@admin.register(Inscription)
class InscriptionAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'telephone', 'niveau', 'statut', 'created_at')
    list_filter = ('statut', 'niveau', 'created_at')
    search_fields = ('nom', 'email', 'telephone')
    filter_horizontal = ('formations',)
    readonly_fields = ('created_at', 'updated_at')
