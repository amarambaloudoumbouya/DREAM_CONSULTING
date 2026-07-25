from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class MessageContact(models.Model):
    STATUT_CHOICES = (
        ('nouveau', 'Nouveau'),
        ('en_cours', 'En cours'),
        ('repondu', 'Répondu'),
        ('archive', 'Archivé'),
    )

    nom_complet = models.CharField(max_length=150, verbose_name='Nom complet')
    email = models.EmailField(verbose_name='E-mail')
    telephone = models.CharField(max_length=30, verbose_name='Téléphone')
    sujet = models.CharField(
        max_length=200,
        verbose_name='Sujet / type de projet',
        help_text='Ex. : mariage, portrait, événement…',
    )
    message = models.TextField(verbose_name='Message')
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouveau',
        verbose_name='Statut',
    )
    reponse = models.TextField(
        blank=True,
        verbose_name='Réponse au client',
        help_text='Message envoyé au client depuis le back-office.',
    )
    reponse_envoyee_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name='Réponse envoyée le',
    )
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'message de contact'
        verbose_name_plural = 'messages de contact'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nom_complet} — {self.sujet}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nom_complet) or slugify(self.email)
            self.slug = f'{base}-{get_random_string(5)}'
        super().save(*args, **kwargs)
