from django.db import migrations


SLIDES = [
    {
        'surtitre': "Capturez l'instant, vivez l'émotion !",
        'ligne_1_avant': '',
        'ligne_1_accent': 'Dream Consulting Com',
        'ligne_1_apres': '',
        'ligne_2_avant': 'Photographie & Événementiel',
        'ligne_2_accent': '',
        'ligne_2_apres': '',
        'description': (
            'Nous immortalisons vos moments les plus précieux et sublimons vos événements\n'
            'avec créativité, passion et professionnalisme.'
        ),
        'image_statique': 'front/assets/img/slider/dream_slider_1.jpeg',
        'bouton_texte': 'Nos Services',
        'bouton_lien': '/photographie/',
        'overlay': 'overlay-2',
        'ordre': 0,
        'is_active': True,
    },
    {
        'surtitre': 'Chaque image raconte une histoire',
        'ligne_1_avant': 'Des Souvenirs',
        'ligne_1_accent': '',
        'ligne_1_apres': '',
        'ligne_2_avant': '',
        'ligne_2_accent': 'Inoubliables',
        'ligne_2_apres': ' pour Toujours',
        'description': (
            "Mariages, portraits, cérémonies ou événements d'entreprise : nous mettons notre talent\n"
            'au service de vos plus beaux instants.'
        ),
        'image_statique': 'front/assets/img/slider/dream_slider_2.jpeg',
        'bouton_texte': 'Nos Services',
        'bouton_lien': '/photographie/',
        'overlay': 'overlay-4',
        'ordre': 1,
        'is_active': True,
    },
    {
        'surtitre': 'Votre vision, notre objectif',
        'ligne_1_avant': 'Sublimons ',
        'ligne_1_accent': 'Ensemble',
        'ligne_1_apres': '',
        'ligne_2_avant': 'Vos Événements',
        'ligne_2_accent': '',
        'ligne_2_apres': '',
        'description': (
            'De la conception à la réalisation, nous créons des expériences uniques\n'
            'et des images d\'exception qui vous ressemblent.'
        ),
        'image_statique': 'front/assets/img/slider/dream_slider_3.jpeg',
        'bouton_texte': 'Nos Services',
        'bouton_lien': '/photographie/',
        'overlay': 'overlay-4',
        'ordre': 2,
        'is_active': True,
    },
]


def seed_sliders(apps, schema_editor):
    Slider = apps.get_model('slider', 'Slider')
    if Slider.objects.exists():
        return
    for data in SLIDES:
        Slider.objects.create(**data)


def unseed_sliders(apps, schema_editor):
    Slider = apps.get_model('slider', 'Slider')
    Slider.objects.filter(
        image_statique__startswith='front/assets/img/slider/dream_slider_'
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_sliders, unseed_sliders),
    ]
