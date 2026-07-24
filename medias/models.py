from django.db import models
from django.templatetags.static import static


class Photographie(models.Model):
    categorie = models.CharField(
        max_length=100,
        verbose_name='Catégorie',
        help_text='Ex. : Mariage, Portrait, Événement. Plusieurs photos peuvent partager la même catégorie.',
        db_index=True,
    )
    titre = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre affiché sur la photo. Ex. : Cérémonie de mariage',
    )
    image = models.ImageField(
        upload_to='medias/photographies/',
        blank=True,
        verbose_name='Image',
        help_text='Photo de la galerie. Si vide, l’image de secours est utilisée.',
    )
    image_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image static (secours)',
        help_text='Ex. front/assets/img/gallery/1.jpg',
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordre',
        help_text='0 = première photo, puis 1, 2…',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Actif',
        help_text='Décochez pour masquer cette photo sur le site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'photographie'
        verbose_name_plural = 'photographies'
        ordering = ['ordre', 'id']

    def __str__(self):
        return f'{self.categorie} — {self.titre}'

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        if self.image_statique:
            return static(self.image_statique)
        return ''

    @property
    def categorie_slug(self):
        from django.utils.text import slugify
        return slugify(self.categorie) or 'autre'


class Branding(models.Model):
    categorie = models.CharField(
        max_length=100,
        verbose_name='Catégorie',
        help_text='Ex. : Réseaux sociaux, Reels, Promo',
    )
    titre = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre affiché sur le visuel. Ex. : Teaser de mariage',
    )
    image = models.ImageField(
        upload_to='medias/branding/',
        blank=True,
        verbose_name='Image',
        help_text='Visuel branding. Si vide, l’image de secours est utilisée.',
    )
    image_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image static (secours)',
        help_text='Ex. front/assets/img/gallery/1.jpg',
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordre',
        help_text='0 = premier visuel, puis 1, 2…',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Actif',
        help_text='Décochez pour masquer ce visuel sur le site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'branding'
        verbose_name_plural = 'brandings'
        ordering = ['ordre', 'id']

    def __str__(self):
        return self.titre

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        if self.image_statique:
            return static(self.image_statique)
        return ''


class WebDesign(models.Model):
    categorie = models.CharField(
        max_length=100,
        verbose_name='Catégorie',
        help_text='Ex. : Site vitrine, E-commerce, Landing page',
    )
    titre = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre du projet. Ex. : Site web restaurant',
    )
    description = models.TextField(
        blank=True,
        verbose_name='Description',
        help_text='Courte description du projet web.',
    )
    image = models.ImageField(
        upload_to='medias/web_design/',
        blank=True,
        verbose_name='Image',
        help_text='Aperçu du projet. Si vide, l’image de secours est utilisée.',
    )
    image_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Image static (secours)',
        help_text='Ex. front/assets/img/gallery/1.jpg',
    )
    url_projet = models.URLField(
        blank=True,
        verbose_name='URL du projet',
        help_text='Lien vers le site en ligne (optionnel).',
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordre',
        help_text='0 = premier projet, puis 1, 2…',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Actif',
        help_text='Décochez pour masquer ce projet sur le site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'web design'
        verbose_name_plural = 'web designs'
        ordering = ['ordre', 'id']

    def __str__(self):
        return self.titre

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        if self.image_statique:
            return static(self.image_statique)
        return ''


class Video(models.Model):
    categorie = models.CharField(
        max_length=100,
        verbose_name='Catégorie',
        help_text='Ex. : Mariage, Cérémonie, Corporate',
    )
    titre = models.CharField(
        max_length=200,
        verbose_name='Titre',
        help_text='Titre affiché sous la vidéo. Ex. : Film de mariage',
    )
    video = models.FileField(
        upload_to='medias/videos/',
        blank=True,
        verbose_name='Fichier vidéo',
        help_text='Fichier MP4 (ou similaire). Si vide, la vidéo de secours est utilisée.',
    )
    video_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Vidéo static (secours)',
        help_text='Ex. front/assets/video/hero-video.mp4',
    )
    poster = models.ImageField(
        upload_to='medias/videos/posters/',
        blank=True,
        verbose_name='Image de couverture (poster)',
        help_text='Image affichée avant la lecture de la vidéo.',
    )
    poster_statique = models.CharField(
        max_length=255,
        blank=True,
        verbose_name='Poster static (secours)',
        help_text='Ex. front/assets/img/gallery/1.jpg',
    )
    ordre = models.PositiveIntegerField(
        default=0,
        verbose_name='Ordre',
        help_text='0 = première vidéo, puis 1, 2…',
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='Actif',
        help_text='Décochez pour masquer cette vidéo sur le site.',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'vidéo'
        verbose_name_plural = 'vidéos'
        ordering = ['ordre', 'id']

    def __str__(self):
        return self.titre

    @property
    def video_url(self):
        if self.video:
            return self.video.url
        if self.video_statique:
            return static(self.video_statique)
        return ''

    @property
    def poster_url(self):
        if self.poster:
            return self.poster.url
        if self.poster_statique:
            return static(self.poster_statique)
        return ''
