from django import forms

from .models import Partenaire


class PartenaireForm(forms.ModelForm):
    class Meta:
        model = Partenaire
        fields = ['nom', 'logo', 'site_web', 'ordre', 'is_active']
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du partenaire',
            }),
            'logo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'site_web': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://…',
            }),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
