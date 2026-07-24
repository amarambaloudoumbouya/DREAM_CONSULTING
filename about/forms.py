from django import forms

from .models import AboutAccordion, AboutCounter, AboutSection, AboutTimeline


class AboutSectionForm(forms.ModelForm):
    class Meta:
        model = AboutSection
        fields = [
            'titre',
            'sous_titre_debut',
            'mot_accent',
            'sous_titre_fin',
            'introduction',
            'image',
            'bouton_texte',
            'is_active',
        ]
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Capturons Aujourd'hui",
            }),
            'sous_titre_debut': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Vos Plus',
            }),
            'mot_accent': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Beaux',
            }),
            'sous_titre_fin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Souvenirs',
            }),
            'introduction': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'bouton_texte': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'À propos',
            }),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AboutAccordionForm(forms.ModelForm):
    class Meta:
        model = AboutAccordion
        fields = ['titre', 'contenu', 'ordre', 'is_active']
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Notre Histoire',
            }),
            'contenu': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Texte du panneau…',
            }),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AboutCounterForm(forms.ModelForm):
    class Meta:
        model = AboutCounter
        fields = ['valeur', 'label', 'is_highlight', 'ordre', 'is_active']
        widgets = {
            'valeur': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'placeholder': '500',
            }),
            'label': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Événements couverts',
            }),
            'is_highlight': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class AboutTimelineForm(forms.ModelForm):
    class Meta:
        model = AboutTimeline
        fields = ['annee', 'titre', 'description', 'image', 'ordre', 'is_active']
        widgets = {
            'annee': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2020',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Année de création',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Description de l’étape…',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
