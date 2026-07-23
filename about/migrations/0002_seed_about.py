from django.db import migrations


HISTOIRE = (
    "Née d'une passion pour l'image et l'émotion, notre entreprise s'est spécialisée "
    "dans la photographie et l'organisation d'événements. Au fil des années, nous avons "
    "accompagné de nombreux clients lors de leurs moments les plus précieux : mariages, "
    "cérémonies, portraits, événements d'entreprise et bien plus encore. Chaque projet "
    "est pour nous une nouvelle histoire à raconter à travers l'objectif.\n"
    "Chez Dream Consulting Com, nous mettons notre savoir-faire, notre créativité et "
    "notre matériel professionnel au service de vos souvenirs, afin de capturer chaque "
    "instant avec authenticité et élégance."
)

MISSION = (
    "Notre mission est d'immortaliser vos moments les plus précieux et de faire de "
    "chacun de vos événements une réussite mémorable. Nous mettons tout notre talent "
    "au service de la mise en valeur de vos émotions, avec des images d'une qualité "
    "irréprochable.\n"
    "Qu'il s'agisse d'un mariage, d'un anniversaire, d'un shooting professionnel ou "
    "d'un événement d'entreprise, nous vous accompagnons de la préparation à la "
    "livraison finale, pour vous offrir une expérience fluide et des souvenirs qui "
    "traversent le temps."
)

VISION = (
    "Notre vision est de devenir une référence incontournable dans le domaine de la "
    "photographie et de l'événementiel, reconnue pour sa créativité, son "
    "professionnalisme et la qualité de ses réalisations.\n"
    "Nous aspirons à créer des œuvres visuelles uniques qui racontent vos histoires "
    "et suscitent l'émotion, tout en repoussant sans cesse les limites de notre art "
    "pour offrir à chaque client une expérience et des souvenirs d'exception."
)


def seed_about(apps, schema_editor):
    AboutSection = apps.get_model('about', 'AboutSection')
    AboutAccordion = apps.get_model('about', 'AboutAccordion')

    AboutSection.objects.get_or_create(
        pk=1,
        defaults={
            'titre': "Capturons Aujourd'hui",
            'sous_titre_debut': 'Vos Plus',
            'mot_accent': 'Beaux',
            'sous_titre_fin': 'Souvenirs',
            'introduction': (
                'Nous immortalisons vos émotions, sublimons vos événements '
                'et créons des souvenirs inoubliables pour toute une vie.'
            ),
            'bouton_texte': 'À propos',
            'is_active': True,
        },
    )

    panels = [
        ('Notre Histoire', HISTOIRE, 0),
        ('Notre Mission', MISSION, 1),
        ('Notre Vision', VISION, 2),
    ]
    for titre, contenu, ordre in panels:
        AboutAccordion.objects.get_or_create(
            titre=titre,
            defaults={'contenu': contenu, 'ordre': ordre, 'is_active': True},
        )


def unseed_about(apps, schema_editor):
    AboutSection = apps.get_model('about', 'AboutSection')
    AboutAccordion = apps.get_model('about', 'AboutAccordion')
    AboutAccordion.objects.filter(
        titre__in=['Notre Histoire', 'Notre Mission', 'Notre Vision']
    ).delete()
    AboutSection.objects.filter(pk=1).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_about, unseed_about),
    ]
