from django.db import migrations


PHOTOGRAPHIES = [
    ('Mariage', 'Cérémonie de mariage', 'front/assets/img/gallery/1.jpg', 0),
    ('Portrait', 'Séance en studio', 'front/assets/img/gallery/2.jpg', 1),
    ('Événement', "Événement d'entreprise", 'front/assets/img/gallery/3.jpg', 2),
    ('Cérémonie', 'Reportage de cérémonie', 'front/assets/img/gallery/4.jpg', 3),
    ('Portrait', 'Portrait lifestyle', 'front/assets/img/gallery/5.jpg', 4),
    ('Fête', 'Anniversaire', 'front/assets/img/gallery/6.jpg', 5),
    ('Mariage', 'Couple de mariés', 'front/assets/img/project/1-1.jpg', 6),
    ('Studio', 'Portrait professionnel', 'front/assets/img/project/1-2.jpg', 7),
    ('Événement', 'Soirée événementielle', 'front/assets/img/project/1-3.jpg', 8),
]

BRANDINGS = [
    ('Réseaux sociaux', 'Teaser de mariage', 'front/assets/img/gallery/1.jpg', 0),
    ('Reels', "Aftermovie d'événement", 'front/assets/img/gallery/2.jpg', 1),
    ('Promo', 'Spot publicitaire', 'front/assets/img/gallery/3.jpg', 2),
    ('Portrait', 'Behind the scenes', 'front/assets/img/gallery/4.jpg', 3),
    ('Corporate', "Présentation d'entreprise", 'front/assets/img/gallery/5.jpg', 4),
    ('Story', 'Capsule événementielle', 'front/assets/img/gallery/6.jpg', 5),
]

VIDEOS = [
    ('Mariage', 'Film de mariage', 'front/assets/video/hero-video.mp4', 'front/assets/img/gallery/1.jpg', 0),
    ('Cérémonie', 'Reportage de cérémonie', 'front/assets/video/about-video.mp4', 'front/assets/img/gallery/2.jpg', 1),
    ('Événement', "Couverture d'événement", 'front/assets/video/hero-video.mp4', 'front/assets/img/gallery/3.jpg', 2),
    ('Corporate', 'Film institutionnel', 'front/assets/video/about-video.mp4', 'front/assets/img/gallery/4.jpg', 3),
    ('Interview', 'Témoignage vidéo', 'front/assets/video/hero-video.mp4', 'front/assets/img/gallery/5.jpg', 4),
    ('Anniversaire', "Film d'anniversaire", 'front/assets/video/about-video.mp4', 'front/assets/img/gallery/6.jpg', 5),
]


def seed_medias(apps, schema_editor):
    Photographie = apps.get_model('medias', 'Photographie')
    Branding = apps.get_model('medias', 'Branding')
    Video = apps.get_model('medias', 'Video')

    if not Photographie.objects.exists():
        for categorie, titre, image_statique, ordre in PHOTOGRAPHIES:
            Photographie.objects.create(
                categorie=categorie,
                titre=titre,
                image_statique=image_statique,
                ordre=ordre,
                is_active=True,
            )

    if not Branding.objects.exists():
        for categorie, titre, image_statique, ordre in BRANDINGS:
            Branding.objects.create(
                categorie=categorie,
                titre=titre,
                image_statique=image_statique,
                ordre=ordre,
                is_active=True,
            )

    if not Video.objects.exists():
        for categorie, titre, video_statique, poster_statique, ordre in VIDEOS:
            Video.objects.create(
                categorie=categorie,
                titre=titre,
                video_statique=video_statique,
                poster_statique=poster_statique,
                ordre=ordre,
                is_active=True,
            )


def unseed_medias(apps, schema_editor):
    Photographie = apps.get_model('medias', 'Photographie')
    Branding = apps.get_model('medias', 'Branding')
    Video = apps.get_model('medias', 'Video')
    Photographie.objects.all().delete()
    Branding.objects.all().delete()
    Video.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_medias, unseed_medias),
    ]
