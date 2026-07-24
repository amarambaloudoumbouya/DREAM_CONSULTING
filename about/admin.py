from django.contrib import admin

from .models import AboutAccordion, AboutCounter, AboutSection, AboutTimeline


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


@admin.register(AboutCounter)
class AboutCounterAdmin(admin.ModelAdmin):
    list_display = ('label', 'valeur', 'ordre', 'is_highlight', 'is_active', 'updated_at')
    list_filter = ('is_active', 'is_highlight')
    list_editable = ('ordre', 'valeur', 'is_highlight', 'is_active')
    search_fields = ('label',)
    readonly_fields = ('created_at', 'updated_at')


@admin.register(AboutTimeline)
class AboutTimelineAdmin(admin.ModelAdmin):
    list_display = ('annee', 'titre', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active',)
    list_editable = ('ordre', 'is_active')
    search_fields = ('annee', 'titre', 'description')
    readonly_fields = ('created_at', 'updated_at')
