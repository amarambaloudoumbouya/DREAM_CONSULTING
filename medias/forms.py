import uuid

from django import forms

from .models import Branding, Photographie, Video, WebDesign


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

    def value_from_datadict(self, data, files, name):
        if hasattr(files, 'getlist'):
            return files.getlist(name)
        value = files.get(name)
        if value:
            return [value]
        return []


class MultipleFileField(forms.FileField):
    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(item, initial) for item in data if item]
        elif data:
            result = [single_file_clean(data, initial)]
        else:
            result = []
        if self.required and not result:
            raise forms.ValidationError(self.error_messages['required'], code='required')
        return result


class PhotographieForm(forms.ModelForm):
    class Meta:
        model = Photographie
        fields = ['categorie', 'titre', 'image', 'ordre', 'is_active']
        widgets = {
            'categorie': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Mariage',
                'list': 'photographie-categories',
            }),
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cérémonie de mariage',
            }),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class PhotographieCreateForm(forms.Form):
    """Ajout d'une ou plusieurs photos dans une même catégorie."""

    categorie = forms.CharField(
        label='Catégorie',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mariage',
            'list': 'photographie-categories',
        }),
        help_text='Réutilisez une catégorie existante pour regrouper plusieurs photos.',
    )
    titre = forms.CharField(
        label='Titre',
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cérémonie de mariage',
        }),
        help_text='Si plusieurs images : le titre sera suivi de (1), (2)…',
    )
    images = MultipleFileField(
        label='Image(s)',
        widget=MultipleFileInput(attrs={
            'class': 'form-control',
            'accept': 'image/*',
        }),
        help_text='Vous pouvez sélectionner plusieurs photos à la fois pour cette catégorie.',
    )
    ordre = forms.IntegerField(
        label='Ordre',
        min_value=0,
        initial=0,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
    )
    is_active = forms.BooleanField(
        label='Actif',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )

    def save(self):
        categorie = self.cleaned_data['categorie'].strip()
        titre = self.cleaned_data['titre'].strip()
        images = self.cleaned_data['images']
        ordre = self.cleaned_data['ordre']
        is_active = self.cleaned_data['is_active']
        groupe_id = uuid.uuid4()
        created = []
        total = len(images)
        for index, image in enumerate(images):
            photo_titre = f'{titre} ({index + 1})' if total > 1 else titre
            created.append(Photographie.objects.create(
                categorie=categorie,
                titre=photo_titre,
                image=image,
                groupe_id=groupe_id,
                ordre=ordre + index,
                is_active=is_active,
            ))
        return created


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
            'video': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'video/mp4,video/webm,video/quicktime,video/*',
            }),
            'poster': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*',
            }),
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
