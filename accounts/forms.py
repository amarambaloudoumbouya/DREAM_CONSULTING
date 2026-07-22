from django import forms

from .models import CustomerUser


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
    )
    password_confirm = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
    )

    class Meta:
        model = CustomerUser
        fields = ['prenoms', 'nom', 'sexe', 'role', 'email', 'tel', 'photo']
        widgets = {
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s)'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Les mots de passe ne correspondent pas.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['prenoms', 'nom', 'sexe', 'role', 'email', 'tel', 'photo']
        widgets = {
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s)'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'role': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class MembreCreateForm(forms.ModelForm):
    password = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
    )
    password_confirm = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe',
        }),
    )

    class Meta:
        model = CustomerUser
        fields = [
            'prenoms', 'nom', 'sexe', 'email', 'tel',
            'fonction_poste', 'photo',
            'reseau_social_facebook', 'reseau_social_twitter',
            'reseau_social_linkedin', 'reseau_social_youtube',
        ]
        widgets = {
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s)'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'fonction_poste': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. Photographe, Vidéaste…',
            }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'reseau_social_facebook': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://facebook.com/...',
            }),
            'reseau_social_twitter': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://twitter.com/...',
            }),
            'reseau_social_linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/...',
            }),
            'reseau_social_youtube': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://youtube.com/...',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', 'Les mots de passe ne correspondent pas.')
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'membre'
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class MembreUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = [
            'prenoms', 'nom', 'sexe', 'email', 'tel',
            'fonction_poste', 'photo', 'is_active',
            'reseau_social_facebook', 'reseau_social_twitter',
            'reseau_social_linkedin', 'reseau_social_youtube',
        ]
        widgets = {
            'prenoms': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom(s)'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'sexe': forms.Select(attrs={'class': 'form-select'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'tel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'fonction_poste': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex. Photographe, Vidéaste…',
            }),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'reseau_social_facebook': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://facebook.com/...',
            }),
            'reseau_social_twitter': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://twitter.com/...',
            }),
            'reseau_social_linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/...',
            }),
            'reseau_social_youtube': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://youtube.com/...',
            }),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'membre'
        if commit:
            user.save()
        return user
