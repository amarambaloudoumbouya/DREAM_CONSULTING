from django.db import migrations


FORMATIONS = [
    {
        'titre': 'Photographie',
        'slug': 'photographie',
        'icone': 'la-camera-retro',
        'duree': '3 à 5 jours',
        'niveau': 'Débutant → Confirmé',
        'description': 'Maîtrisez la prise de vue, la lumière, la composition et le retouche pour produire des images professionnelles.',
        'points': ['Portrait & studio', 'Mariage & événement', 'Lightroom & workflow'],
        'image': 'front/assets/img/gallery/1.jpg',
        'ordre': 1,
    },
    {
        'titre': 'Vidéographie',
        'slug': 'videographie',
        'icone': 'la-video',
        'duree': '4 à 6 jours',
        'niveau': 'Débutant → Intermédiaire',
        'description': 'De la captation au montage : apprenez à raconter une histoire en images animées.',
        'points': ['Cadre & mouvement', 'Son & lumière', 'Montage & colorimétrie'],
        'image': 'front/assets/img/gallery/2.jpg',
        'ordre': 2,
    },
    {
        'titre': 'Design graphique / Branding',
        'slug': 'design-branding',
        'icone': 'la-palette',
        'duree': '3 à 4 jours',
        'niveau': 'Tous niveaux',
        'description': 'Construisez une identité visuelle forte : logo, charte, supports print et digitaux.',
        'points': ['Identité de marque', 'Composition visuelle', 'Supports réseaux sociaux'],
        'image': 'front/assets/img/gallery/3.jpg',
        'ordre': 3,
    },
    {
        'titre': 'Motion Design',
        'slug': 'motion-design',
        'icone': 'la-film',
        'duree': '4 à 5 jours',
        'niveau': 'Intermédiaire',
        'description': 'Animez vos créations : intros, motion logos, capsules publicitaires et contenus dynamiques.',
        'points': ['After Effects', 'Animation 2D', 'Storyboard & rythme'],
        'image': 'front/assets/img/gallery/4.jpg',
        'ordre': 4,
    },
    {
        'titre': 'Drone',
        'slug': 'drone',
        'icone': 'la-helicopter',
        'duree': '2 à 3 jours',
        'niveau': 'Débutant → Confirmé',
        'description': 'Pilotez en sécurité et capturez des plans aériens cinématographiques pour vos projets.',
        'points': ['Réglementation & sécurité', 'Plans aériens', 'Prise de vue événementielle'],
        'image': 'front/assets/img/gallery/5.jpg',
        'ordre': 5,
    },
]


def seed_formations(apps, schema_editor):
    Formation = apps.get_model('formation', 'Formation')
    for data in FORMATIONS:
        Formation.objects.update_or_create(slug=data['slug'], defaults=data)


def unseed_formations(apps, schema_editor):
    Formation = apps.get_model('formation', 'Formation')
    Formation.objects.filter(slug__in=[f['slug'] for f in FORMATIONS]).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial_formations'),
    ]

    operations = [
        migrations.RunPython(seed_formations, unseed_formations),
    ]
