from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class Collaborateur(models.Model):
    titre = models.CharField(
        max_length=150,
        verbose_name='Titre / projet',
        help_text='Ex. CRICT, Portrait Studio, Cérémonie…',
    )
    sous_titre = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Sous-titre',
        help_text='Ex. Nom du client, Voir plus…',
    )
    image = models.ImageField(upload_to='collaborateurs/', verbose_name='Image')
    lien = models.URLField(blank=True, verbose_name='Lien')
    ordre = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'collaborateur'
        verbose_name_plural = 'collaborateurs'
        ordering = ['ordre', 'titre']

    def __str__(self):
        return self.titre

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.titre) or 'collaborateur'
            self.slug = f'{base}-{get_random_string(5)}'
        super().save(*args, **kwargs)
