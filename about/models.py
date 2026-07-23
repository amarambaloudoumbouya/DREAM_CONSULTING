from django.db import models


class AboutSection(models.Model):
    """Contenu unique de la section À propos (page d'accueil)."""

    titre = models.CharField(
        max_length=200,
        default="Capturons Aujourd'hui",
        verbose_name='Titre (ligne 1)',
    )
    sous_titre_debut = models.CharField(
        max_length=100,
        default='Vos Plus',
        verbose_name='Sous-titre (avant le mot mis en avant)',
    )
    mot_accent = models.CharField(
        max_length=50,
        default='Beaux',
        verbose_name='Mot mis en avant',
        help_text='Affiché dans un <span> sur le site.',
    )
    sous_titre_fin = models.CharField(
        max_length=100,
        default='Souvenirs',
        verbose_name='Sous-titre (après le mot mis en avant)',
    )
    introduction = models.TextField(
        verbose_name='Introduction',
        default=(
            'Nous immortalisons vos émotions, sublimons vos événements '
            'et créons des souvenirs inoubliables pour toute une vie.'
        ),
    )
    image = models.ImageField(
        upload_to='about/',
        blank=True,
        verbose_name='Image',
    )
    bouton_texte = models.CharField(
        max_length=50,
        default='À propos',
        verbose_name='Texte du bouton',
    )
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'section à propos'
        verbose_name_plural = 'section à propos'

    def __str__(self):
        return 'Section À propos'

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        return ''

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj


class AboutAccordion(models.Model):
    """Panneau d'accordéon (ex. Notre Histoire, Notre Mission, Notre Vision)."""

    titre = models.CharField(max_length=150, verbose_name='Titre')
    contenu = models.TextField(verbose_name='Contenu')
    ordre = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'panneau à propos'
        verbose_name_plural = 'panneaux à propos'
        ordering = ['ordre', 'titre']

    def __str__(self):
        return self.titre
