from django import forms

from .models import Slider


class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = [
            'surtitre',
            'ligne_1_avant',
            'ligne_1_accent',
            'ligne_1_apres',
            'ligne_2_avant',
            'ligne_2_accent',
            'ligne_2_apres',
            'description',
            'image',
            'bouton_texte',
            'bouton_lien',
            'overlay',
            'ordre',
            'is_active',
        ]
        widgets = {
            'surtitre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Capturez l'instant, vivez l'émotion !",
            }),
            'ligne_1_avant': forms.TextInput(attrs={'class': 'form-control'}),
            'ligne_1_accent': forms.TextInput(attrs={'class': 'form-control'}),
            'ligne_1_apres': forms.TextInput(attrs={'class': 'form-control'}),
            'ligne_2_avant': forms.TextInput(attrs={'class': 'form-control'}),
            'ligne_2_accent': forms.TextInput(attrs={'class': 'form-control'}),
            'ligne_2_apres': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bouton_texte': forms.TextInput(attrs={'class': 'form-control'}),
            'bouton_lien': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '/photographie/',
            }),
            'overlay': forms.Select(attrs={'class': 'form-select'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
