from django.db import models
from django.utils.crypto import get_random_string
from django.utils.text import slugify


class Formation(models.Model):
    titre = models.CharField(max_length=150, verbose_name='Titre')
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    icone = models.CharField(
        max_length=50,
        default='la-graduation-cap',
        verbose_name='Icône Line Awesome',
        help_text='Ex: la-camera-retro',
    )
    duree = models.CharField(max_length=100, verbose_name='Durée')
    niveau = models.CharField(max_length=100, verbose_name='Niveau')
    description = models.TextField(verbose_name='Description')
    points = models.JSONField(default=list, blank=True, verbose_name='Points clés')
    image = models.ImageField(
        upload_to='formations/images/',
        blank=True,
        null=True,
        verbose_name='Image de la formation',
    )
    image_url = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image de la formation URL',
        help_text='Ex: front/assets/img/gallery/1.jpg',
    )
    ordre = models.PositiveIntegerField(default=0, verbose_name='Ordre')
    is_active = models.BooleanField(default=True, verbose_name='Active')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'formation'
        verbose_name_plural = 'formations'
        ordering = ['ordre', 'titre']

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)
        super().save(*args, **kwargs)

    @property
    def photo_url(self):
        if self.image:
            return self.image.url
        if not self.image_url:
            return ''
        if self.image_url.startswith(('http://', 'https://', '/')):
            return self.image_url
        from django.templatetags.static import static
        return static(self.image_url)


class Inscription(models.Model):
    NIVEAU_CHOICES = (
        ('debutant', 'Débutant'),
        ('intermediaire', 'Intermédiaire'),
        ('confirme', 'Confirmé'),
    )
    STATUT_CHOICES = (
        ('nouvelle', 'Nouvelle'),
        ('confirmee', 'Confirmée'),
        ('refusee', 'Refusée'),
    )

    nom = models.CharField(max_length=150, verbose_name='Nom')
    prenom = models.CharField(max_length=150, blank=True, default='', verbose_name='Prénom')
    telephone = models.CharField(max_length=30, verbose_name='Téléphone')
    email = models.EmailField(verbose_name='E-mail')
    niveau = models.CharField(max_length=20, choices=NIVEAU_CHOICES, verbose_name='Niveau')
    formations = models.ManyToManyField(
        Formation,
        related_name='inscriptions',
        verbose_name='Formations',
    )
    message = models.TextField(blank=True, verbose_name='Message / objectifs')
    statut = models.CharField(
        max_length=20,
        choices=STATUT_CHOICES,
        default='nouvelle',
        verbose_name='Statut',
    )
    slug = models.SlugField(max_length=255, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'inscription'
        verbose_name_plural = 'inscriptions'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nom} — {self.email}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base = slugify(f'{self.prenom} {self.nom}'.strip()) or slugify(self.email)
            self.slug = f'{base}-{get_random_string(5)}'
        super().save(*args, **kwargs)
