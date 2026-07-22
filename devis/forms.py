from django import forms

from .models import DemandeDevis


class DemandeDevisForm(forms.ModelForm):
    prestations = forms.MultipleChoiceField(
        choices=DemandeDevis.PRESTATION_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        required=True,
        label='Type de prestation',
        error_messages={'required': 'Veuillez sélectionner au moins une prestation.'},
    )

    class Meta:
        model = DemandeDevis
        fields = [
            'nom_complet',
            'lieu',
            'telephone',
            'email',
            'prestations',
            'type_evenement',
            'date_evenement',
            'heure',
        ]
        widgets = {
            'nom_complet': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom complet',
            }),
            'lieu': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ville / Lieu',
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numéro de téléphone',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'E-mail',
            }),
            'type_evenement': forms.Select(attrs={
                'class': 'form-control form-dropdown select_option wide',
            }),
            'date_evenement': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
            }),
            'heure': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type_evenement'].choices = [('', "Choisir un événement")] + list(
            DemandeDevis.EVENT_CHOICES
        )
        self.fields['nom_complet'].label = 'Nom complet'
        self.fields['lieu'].label = "Lieu de l'événement"
        self.fields['telephone'].label = 'Numéro de téléphone'
        self.fields['email'].label = 'E-mail'
        self.fields['type_evenement'].label = "Type d'événement"
        self.fields['date_evenement'].label = "Date de l'événement"
        self.fields['heure'].label = 'Heure'


class RetourDevisForm(forms.Form):
    statut = forms.ChoiceField(
        choices=DemandeDevis.STATUT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Statut',
    )
    retour = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre retour / proposition au client…',
        }),
        label='Retour au client',
    )
    envoyer_email = forms.BooleanField(
        required=False,
        initial=True,
        label='Envoyer le retour par email au client',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),)
