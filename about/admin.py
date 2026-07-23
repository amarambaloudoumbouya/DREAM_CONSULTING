from django.contrib import admin

from .models import AboutAccordion, AboutSection


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'is_active', 'updated_at')
    readonly_fields = ('updated_at',)


@admin.register(AboutAccordion)
class AboutAccordionAdmin(admin.ModelAdmin):
    list_display = ('titre', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('ordre', 'is_active')
    search_fields = ('titre', 'contenu')
    readonly_fields = ('created_at', 'updated_at')
