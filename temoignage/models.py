from django.db import models
from django.utils import timezone
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class Temoignage(models.Model):
    STATUT_CHOICES = (
        ('en_attente', 'En attente'),
        ('publie', 'Publié'),
        ('refuse', 'Refusé'),
    )

    nom = models.CharField(max_length=150, verbose_name='Nom')
    prenom = models.CharField(max_length=150, blank=True, default='', verbose_name='Prénom')
    email = models.EmailField(blank=True, verbose_name='E-mail')
    fonction = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Fonction / qualité',
        help_text='Ex. Mariée, Directeur, Client…',
    )
    photo = models.ImageField(
        upload_to='temoignages/',
        blank=True,
        null=True,
        verbose_name='Photo',
    )
    avis = models.TextField(verbose_name='Avis / témoignage')
    note = models.PositiveSmallIntegerField(
        default=5,
        verbose_name='Note',
        help_text='Note de 1 à 5',
    )
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='en_attente',
        verbose_name='Statut',
    )
    publie_at = models.DateTimeField(blank=True, null=True, verbose_name='Publié le')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'témoignage'
        verbose_name_plural = 'témoignages'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.full_name} — {self.get_statut_display()}'

    @property
    def full_name(self):
        return f'{self.prenom} {self.nom}'.strip() or self.nom

    @property
    def photo_url(self):
        if self.photo:
            return self.photo.url
        return ''

    def publier(self):
        self.statut = 'publie'
        self.publie_at = timezone.now()
        self.save(update_fields=['statut', 'publie_at', 'updated_at'])

    def refuser(self):
        self.statut = 'refuse'
        self.publie_at = None
        self.save(update_fields=['statut', 'publie_at', 'updated_at'])

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.full_name) or 'temoignage'
            self.slug = f'{base}-{get_random_string(5)}'
        if self.note < 1:
            self.note = 1
        if self.note > 5:
            self.note = 5
        super().save(*args, **kwargs)
