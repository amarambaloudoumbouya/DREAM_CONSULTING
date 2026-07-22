from django import forms

from .models import Temoignage


class TemoignagePublicForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = ['prenom', 'nom', 'email', 'fonction', 'photo', 'avis', 'note']
        widgets = {
            'prenom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom',
            }),
            'nom': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail (optionnel)',
            }),
            'fonction': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. Mariée, Directeur, Client…',
            }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'avis': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Partagez votre expérience avec Dream Consulting Com…',
            }),
            'note': forms.Select(
                choices=[(i, f'{i} / 5') for i in range(5, 0, -1)],
                attrs={'class': 'form-control form-select'},
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['prenom'].label = 'Prénom'
        self.fields['nom'].label = 'Nom'
        self.fields['email'].label = 'E-mail'
        self.fields['email'].required = False
        self.fields['fonction'].label = 'Fonction / qualité'
        self.fields['fonction'].required = False
        self.fields['photo'].label = 'Photo (optionnel)'
        self.fields['photo'].required = False
        self.fields['avis'].label = 'Votre avis'
        self.fields['note'].label = 'Note'


class TemoignageAdminForm(forms.ModelForm):
    class Meta:
        model = Temoignage
        fields = [
            'prenom', 'nom', 'email', 'fonction', 'photo',
            'avis', 'note', 'statut',
        ]
        widgets = {
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'avis': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'note': forms.Select(
                choices=[(i, f'{i} / 5') for i in range(5, 0, -1)],
                attrs={'class': 'form-select'},
            ),
            'statut': forms.Select(attrs={'class': 'form-select'}),
        }
