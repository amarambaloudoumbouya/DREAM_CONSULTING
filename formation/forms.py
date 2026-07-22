from django import forms

from .models import Formation, Inscription


class FormationForm(forms.ModelForm):
    points_text = forms.CharField(
        label='Points clés',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 2,
            'placeholder': 'Un point par ligne',
        }),
        help_text='Saisir un point par ligne.',
    )

    class Meta:
        model = Formation
        fields = [
            'titre',
            'icone',
            'duree',
            'niveau',
            'description',
            'image',
            'ordre',
            'is_active',
        ]
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre de la formation'}),
            'icone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'la-camera-retro'}),
            'duree': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '3 à 5 jours'}),
            'niveau': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Débutant → Confirmé'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'ordre': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.points:
            self.fields['points_text'].initial = '\n'.join(self.instance.points)

    def clean_points_text(self):
        raw = self.cleaned_data.get('points_text', '')
        return [line.strip() for line in raw.splitlines() if line.strip()]

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.points = self.cleaned_data.get('points_text', [])
        if commit:
            instance.save()
        return instance


class InscriptionForm(forms.ModelForm):
    formations = forms.ModelMultipleChoiceField(
        queryset=Formation.objects.filter(is_active=True),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label='Formation(s) souhaitée(s)',
    )

    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'telephone', 'email', 'niveau', 'formations', 'message']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Votre e-mail'}),
            'niveau': forms.Select(attrs={'class': 'form-select wide'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Parlez-nous de vos objectifs, disponibilités, etc.',
                'rows': 2,
            }),
        }

    def __init__(self, *args, **kwargs):
        selected_slug = kwargs.pop('selected_slug', None)
        super().__init__(*args, **kwargs)
        self.fields['formations'].queryset = Formation.objects.filter(is_active=True)
        self.fields['prenom'].required = True
        self.fields['niveau'].choices = [('', 'Choisir un niveau')] + [
            c for c in self.fields['niveau'].choices if c[0]
        ]

        if selected_slug and not self.is_bound:
            selected = Formation.objects.filter(slug=selected_slug, is_active=True)
            self.fields['formations'].initial = list(selected.values_list('pk', flat=True))
