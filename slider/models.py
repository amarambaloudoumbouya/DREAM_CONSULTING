from django.db import models
from django.templatetags.static import static


class Slider(models.Model):
    OVERLAY_CHOICES = [
        ('overlay-2', 'Overlay 2'),
        ('overlay-4', 'Overlay 4'),
    ]

    surtitre = models.CharField(
        max_length=200,
        verbose_name='Surtitre',
        help_text='Petite phrase au-dessus du grand titre. Ex. : Capturez l\'instant, vivez l\'émotion !',
    )
    ligne_1_avant = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 1 (avant accent)',
        help_text='Texte normal avant le mot mis en valeur. Ex. : Sublimons',
    )
    ligne_1_accent = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 1 (mot accentué)',
        help_text='Mot ou expression mis en évidence (couleur). Ex. : Ensemble ou Dream Consulting Com',
    )
    ligne_1_apres = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 1 (après accent)',
        help_text='Texte normal après le mot mis en valeur. Laissez vide si inutile.',
    )
    ligne_2_avant = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 2 (avant accent)',
        help_text='Début de la 2ᵉ ligne du titre. Ex. : Photographie & Événementiel',
    )
    ligne_2_accent = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 2 (mot accentué)',
        help_text='Mot mis en évidence sur la 2ᵉ ligne. Ex. : Inoubliables',
    )
    ligne_2_apres = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Titre ligne 2 (après accent)',
        help_text='Fin de la 2ᵉ ligne. Ex. : pour Toujours',
    )
    description = models.TextField(
        verbose_name='Description',
        help_text='Court paragraphe affiché sous le titre.',
    )
    image = models.ImageField(
        upload_to='sliders/',
        blank=True,
        verbose_name='Image de fond',
        help_text='Photo en arrière-plan du slide. Si vide, l’image de secours est utilisée.',
    )
    image_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image static (secours)',
        help_text='Ex. front/assets/img/slider/dream_slider_1.jpeg — utilisé si aucune image uploadée.',
    )
    bouton_texte = models.CharField(
        max_length=80,
        default='Nos Services',
        verbose_name='Texte du bouton',
        help_text='Libellé du bouton. Ex. : Nos Services',
    )
    bouton_lien = models.CharField(
        max_length=255,
        default='/photographie/',
        verbose_name='Lien du bouton',
        help_text='Page ouverte au clic. Ex. : /photographie/ ou /contact/',
    )
    overlay = models.CharField(
        max_length=20,
        choices=OVERLAY_CHOICES,
        default='overlay-4',
        verbose_name='Overlay',
        help_text='Assombrissement de l’image pour mieux lire le texte (2 = léger, 4 = plus fort).',
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordre',
        help_text='Position dans le carrousel : 0 = premier, puis 1, 2…',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Actif',
        help_text='Décochez pour masquer ce slide sur le site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'slider'
        verbose_name_plural = 'sliders'
        ordering = ['ordre', 'id']

    def __str__(self):
        return self.surtitre

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        if self.image_statique:
            return static(self.image_statique)
        return ''

    @property
    def has_ligne_2(self):
        return bool(self.ligne_2_avant or self.ligne_2_accent or self.ligne_2_apres)
