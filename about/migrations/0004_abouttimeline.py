from django.db import migrations, models


TIMELINES = [
    (
        '2020',
        'Année de création',
        "Dream Consulting Com voit le jour, portée par une passion pour la photographie "
        "et l'envie d'immortaliser les moments les plus précieux de la vie.",
        'front/assets/img/timeline/1.jpg',
        0,
    ),
    (
        '2021',
        'Nos débuts',
        "À nos débuts, nous nous concentrions sur les séances de portraits "
        "et les photos de famille pour les particuliers de notre région.",
        'front/assets/img/timeline/2.jpg',
        1,
    ),
    (
        '2022',
        'Croissance et reconnaissance',
        "Peu à peu, notre travail est reconnu et recommandé, notamment pour "
        "la photographie de mariage, grâce à notre sens du détail et notre créativité.",
        'front/assets/img/timeline/3.jpg',
        2,
    ),
    (
        '2023',
        'Diversification des services',
        "Pour répondre à une demande croissante, nous ajoutons la "
        "vidéographie et l'organisation d'événements à nos prestations.",
        'front/assets/img/timeline/4.jpg',
        3,
    ),
    (
        '2024',
        'Partenariats stratégiques',
        "Nous développons des partenariats solides avec des lieux de "
        "réception, des traiteurs et des professionnels de l'événementiel pour offrir des "
        "prestations complètes.",
        'front/assets/img/timeline/5.jpg',
        4,
    ),
]


def seed_timelines(apps, schema_editor):
    AboutTimeline = apps.get_model('about', 'AboutTimeline')
    if AboutTimeline.objects.exists():
        return
    for annee, titre, description, image_statique, ordre in TIMELINES:
        AboutTimeline.objects.create(
            annee=annee,
            titre=titre,
            description=description,
            image_statique=image_statique,
            ordre=ordre,
            is_active=True,
        )


def unseed_timelines(apps, schema_editor):
    AboutTimeline = apps.get_model('about', 'AboutTimeline')
    AboutTimeline.objects.filter(
        titre__in=[titre for _, titre, _, _, _ in TIMELINES],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_aboutcounter'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('annee', models.CharField(help_text='Ex. : 2020', max_length=20, verbose_name='Année / date')),
                ('titre', models.CharField(max_length=200, verbose_name='Titre')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, help_text='Si vide, l’image de secours est utilisée.', upload_to='about/timeline/', verbose_name='Image')),
                ('image_statique', models.CharField(blank=True, help_text='Ex. front/assets/img/timeline/1.jpg', max_length=255, verbose_name='Image static (secours)')),
                ('ordre', models.PositiveIntegerField(default=0, verbose_name='Ordre')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'étape timeline',
                'verbose_name_plural': 'étapes timeline',
                'ordering': ['ordre', 'id'],
            },
        ),
        migrations.RunPython(seed_timelines, unseed_timelines),
    ]
