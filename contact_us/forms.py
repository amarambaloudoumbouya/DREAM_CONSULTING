from django import forms

from .models import MessageContact


class MessageContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['nom_complet', 'email', 'telephone', 'sujet', 'message']
        widgets = {
            'nom_complet': forms.TextInput(attrs={
                'placeholder': 'Nom complet',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Adresse e-mail',
                'required': True,
            }),
            'telephone': forms.TextInput(attrs={
                'placeholder': 'Numéro de téléphone',
                'required': True,
            }),
            'sujet': forms.TextInput(attrs={
                'placeholder': 'Type de projet (mariage, portrait, événement...)',
                'required': True,
            }),
            'message': forms.Textarea(attrs={
                'cols': 30,
                'rows': 10,
                'placeholder': 'Décrivez-nous votre projet',
                'required': True,
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.label = ''


class ReponseContactForm(forms.Form):
    statut = forms.ChoiceField(
        choices=MessageContact.STATUT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Statut',
    )
    reponse = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 5,
            'placeholder': 'Votre réponse au client…',
        }),
        label='Réponse au client',
    )
    envoyer_email = forms.BooleanField(
        required=False,
        initial=True,
        label='Envoyer la réponse par email au client',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
