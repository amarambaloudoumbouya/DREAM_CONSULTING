from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string


class DemandeDevis(models.Model):
    PRESTATION_CHOICES = (
        ('design_branding', 'Design graphique / Branding'),
        ('drone', 'Drone'),
        ('motion_design', 'Motion Design'),
        ('photographie', 'Photographie'),
        ('videographie', 'Vidéographie'),
    )
    EVENT_CHOICES = (
        ('mariage', 'Mariage'),
        ('portrait', 'Portrait / Studio'),
        ('ceremonie', 'Cérémonie'),
        ('entreprise', "Événement d'entreprise"),
        ('anniversaire', 'Anniversaire / Fête'),
        ('autre', 'Autre'),
    )
    STATUT_CHOICES = (
        ('nouvelle', 'Nouvelle'),
        ('en_analyse', 'En analyse'),
        ('traitee', 'Traitée'),
        ('refusee', 'Refusée'),
    )

    nom_complet      = models.CharField(max_length=150, verbose_name='Nom complet')
    lieu             = models.CharField(max_length=200, verbose_name="Lieu de l'événement")
    telephone        = models.CharField(max_length=30, verbose_name='Téléphone')
    email            = models.EmailField(verbose_name='E-mail')
    prestations      = models.JSONField(default=list, blank=True, verbose_name='Prestations')
    type_evenement   = models.CharField(max_length=30, choices=EVENT_CHOICES, verbose_name="Type d'événement",)
    date_evenement   = models.DateField(verbose_name="Date de l'événement")
    heure            = models.TimeField(verbose_name='Heure')
    statut           = models.CharField(max_length=20, choices=STATUT_CHOICES, default='nouvelle', verbose_name='Statut',)
    retour           = models.TextField(blank=True, verbose_name='Retour au client', help_text='Message envoyé au client après analyse de la demande.',)
    retour_envoye_at = models.DateTimeField(blank=True, null=True, verbose_name='Retour envoyé le',)
    slug             = models.SlugField(max_length=255, unique=True, editable=False)
    created_at       = models.DateTimeField(auto_now_add=True)
    updated_at       = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'demande de devis'
        verbose_name_plural = 'demandes de devis'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nom_complet} — {self.email}'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nom_complet) + '-' + get_random_string(5)
        super(DemandeDevis, self).save(*args, **kwargs)

    def get_prestations_display(self):
        labels = dict(self.PRESTATION_CHOICES)
        return [labels.get(p, p) for p in self.prestations]
