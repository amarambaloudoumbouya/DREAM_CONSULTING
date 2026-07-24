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


class AboutCounter(models.Model):
    """Compteur affiché sur la page À propos."""

    valeur = models.PositiveIntegerField(verbose_name='Valeur')
    label = models.CharField(
        max_length=100,
        verbose_name='Libellé',
        help_text='Ex. : Depuis, Événements couverts',
    )
    is_highlight = models.BooleanField(
        default=False,
        verbose_name='Mise en avant',
        help_text='Style distinct pour ce compteur.',
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'compteur à propos'
        verbose_name_plural = 'compteurs à propos'
        ordering = ['ordre', 'id']

    def __str__(self):
        return f'{self.valeur} — {self.label}'


class AboutTimeline(models.Model):
    """Étape de la frise chronologique (page À propos)."""

    annee = models.CharField(
        max_length=20,
        verbose_name='Année / date',
        help_text='Ex. : 2020',
    )
    titre = models.CharField(max_length=200, verbose_name='Titre')
    description = models.TextField(verbose_name='Description')
    image = models.ImageField(
        upload_to='about/timeline/',
        blank=True,
        verbose_name='Image',
        help_text='Si vide, l’image de secours est utilisée.',
    )
    image_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image static (secours)',
        help_text='Ex. front/assets/img/timeline/1.jpg',
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Actif')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'étape timeline'
        verbose_name_plural = 'étapes timeline'
        ordering = ['ordre', 'id']

    def __str__(self):
        return f'{self.annee} — {self.titre}'

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        if self.image_statique:
            from django.templatetags.static import static
            return static(self.image_statique)
        return ''
