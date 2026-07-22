from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class CustomerUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("L'email est obligatoire.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Le superutilisateur doit avoir is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Le superutilisateur doit avoir is_superuser=True.')
        if not password:
            raise ValueError('Le superutilisateur doit avoir un mot de passe.')

        return self.create_user(email, password, **extra_fields)


class CustomerUser(AbstractBaseUser, PermissionsMixin):
    SEXE = (
        ('Masculin', 'Masculin'),
        ('Féminin', 'Féminin'),
    )
    ROLE = (
        ('admin', 'Administrateur'),
        ('membre', 'Membre'),
        ('client', 'Client'),
    )

    prenoms                = models.CharField(max_length=150, verbose_name='Prénom(s)')
    nom                    = models.CharField(max_length=150, verbose_name='Nom')
    sexe                   = models.CharField(max_length=20, choices=SEXE, blank=True, null=True, verbose_name='Sexe',)
    role                   = models.CharField(max_length=20, choices=ROLE, default='membre', verbose_name='Rôle', )
    email                  = models.EmailField(max_length=255, unique=True, db_index=True, verbose_name='Email',)
    tel                    = models.CharField(max_length=20, unique=True, verbose_name='Téléphone')
    adresse                = models.CharField(max_length=150, blank=True, null=True, verbose_name='Adresse',)
    fonction_poste         = models.CharField(max_length=150, blank=True, null=True, verbose_name='Fonction / poste',)
    photo                  = models.ImageField(upload_to='accounts/', blank=True, null=True, verbose_name='Photo',)
    reseau_social_facebook = models.URLField(blank=True, null=True, verbose_name='Facebook')
    reseau_social_twitter  = models.URLField(blank=True, null=True, verbose_name='Twitter')
    reseau_social_linkedin = models.URLField(blank=True, null=True, verbose_name='LinkedIn')
    reseau_social_youtube  = models.URLField(blank=True, null=True, verbose_name='YouTube')
    is_active              = models.BooleanField(default=True)
    is_staff               = models.BooleanField(default=False)
    slug                   = models.SlugField(max_length=255, unique=True, editable=False, blank=True,)
    created_at             = models.DateTimeField(auto_now_add=True)
    updated_at             = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['prenoms', 'nom', 'tel']

    objects = CustomerUserManager()

    class Meta:
        verbose_name = 'utilisateur'
        verbose_name_plural = 'utilisateurs'
        ordering = ['-created_at']

    def __str__(self):
        return self.full_name

    @property
    def full_name(self):
        return f'{self.prenoms} {self.nom}'.strip()

    @property
    def image_url(self):
        if self.photo:
            return self.photo.url
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.full_name) or slugify(self.email)
            self.slug = f'{base}-{get_random_string(5)}'
        super().save(*args, **kwargs)
