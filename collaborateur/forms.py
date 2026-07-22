from django import forms

from .models import Collaborateur


class CollaborateurForm(forms.ModelForm):
    class Meta:
        model = Collaborateur
        fields = ['titre', 'sous_titre', 'image', 'lien', 'ordre', 'is_active']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. CRICT, Portrait Studio…',
            }),
            'sous_titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. Nom du client, Voir plus…',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'lien': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://…',
            }),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
