from django.contrib import admin

from .models import Partenaire


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'ordre', 'is_active', 'site_web', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('nom',)
    list_editable = ('ordre', 'is_active')
    readonly_fields = ('slug', 'created_at', 'updated_at')
