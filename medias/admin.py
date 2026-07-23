from django.contrib import admin

from .models import Branding, Photographie, Video


@admin.register(Photographie)
class PhotographieAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active', 'categorie')
    list_editable = ('ordre', 'is_active')
    search_fields = ('titre', 'categorie')


@admin.register(Branding)
class BrandingAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active', 'categorie')
    list_editable = ('ordre', 'is_active')
    search_fields = ('titre', 'categorie')


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'ordre', 'is_active', 'updated_at')
    list_filter = ('is_active', 'categorie')
    list_editable = ('ordre', 'is_active')
    search_fields = ('titre', 'categorie')
