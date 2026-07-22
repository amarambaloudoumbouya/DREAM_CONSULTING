from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class Partenaire(models.Model):
    nom        = models.CharField(max_length=150, verbose_name='Nom')
    logo       = models.ImageField(upload_to='partenaires/', verbose_name='Logo')
    site_web   = models.URLField(blank=True, verbose_name='Site web')
    ordre      = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active  = models.BooleanField(default=True, verbose_name='Actif')
    slug       = models.SlugField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'partenaire'
        verbose_name_plural = 'partenaires'
        ordering = ['ordre', 'nom']

    def __str__(self):
        return self.nom

    @property
    def logo_url(self):
        if self.logo:
            return self.logo.url
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(self.nom) or 'partenaire'
            self.slug = f'{base}-{get_random_string(5)}'
        super().save(*args, **kwargs)
