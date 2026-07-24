from django import forms

from .models import Branding, Photographie, Video, WebDesign


class PhotographieForm(forms.ModelForm):
    class Meta:
        model = Photographie
        fields = ['categorie', 'titre', 'image', 'ordre', 'is_active']
        widgets = {
            'categorie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mariage',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cérémonie de mariage',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BrandingForm(forms.ModelForm):
    class Meta:
        model = Branding
        fields = ['categorie', 'titre', 'image', 'ordre', 'is_active']
        widgets = {
            'categorie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Réseaux sociaux',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Teaser de mariage',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = [
            'categorie',
            'titre',
            'video',
            'poster',
            'ordre',
            'is_active',
        ]
        widgets = {
            'categorie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mariage',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Film de mariage',
            }),
            'video': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'poster': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class WebDesignForm(forms.ModelForm):
    class Meta:
        model = WebDesign
        fields = [
            'categorie',
            'titre',
            'description',
            'image',
            'url_projet',
            'ordre',
            'is_active',
        ]
        widgets = {
            'categorie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Site vitrine',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Site web restaurant',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Description du projet',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'url_projet': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://exemple.com',
            }),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
