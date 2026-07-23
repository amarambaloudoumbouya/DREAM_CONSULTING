from django.contrib import admin

from .models import Slider


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('surtitre', 'ordre', 'is_active', 'overlay', 'updated_at')
    list_filter = ('is_active', 'overlay')
    list_editable = ('ordre', 'is_active')
    search_fields = ('surtitre', 'description')
    readonly_fields = ('created_at', 'updated_at')
