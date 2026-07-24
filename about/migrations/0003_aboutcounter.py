from django.db import migrations, models


COUNTERS = [
    (2020, 'Depuis', True, 0),
    (500, 'Événements couverts', False, 1),
    (215, 'Projets réalisés', False, 2),
    (450, 'Clients satisfaits', False, 3),
]


def seed_counters(apps, schema_editor):
    AboutCounter = apps.get_model('about', 'AboutCounter')
    if AboutCounter.objects.exists():
        return
    for valeur, label, is_highlight, ordre in COUNTERS:
        AboutCounter.objects.create(
            valeur=valeur,
            label=label,
            is_highlight=is_highlight,
            ordre=ordre,
            is_active=True,
        )


def unseed_counters(apps, schema_editor):
    AboutCounter = apps.get_model('about', 'AboutCounter')
    AboutCounter.objects.filter(
        label__in=[label for _, label, _, _ in COUNTERS],
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_seed_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutCounter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.PositiveIntegerField(verbose_name='Valeur')),
                ('label', models.CharField(help_text='Ex. : Depuis, Événements couverts', max_length=100, verbose_name='Libellé')),
                ('is_highlight', models.BooleanField(default=False, help_text='Style distinct pour ce compteur.', verbose_name='Mise en avant')),
                ('ordre', models.PositiveIntegerField(default=0, verbose_name='Ordre')),
                ('is_active', models.BooleanField(default=True, verbose_name='Actif')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'compteur à propos',
                'verbose_name_plural': 'compteurs à propos',
                'ordering': ['ordre', 'id'],
            },
        ),
        migrations.RunPython(seed_counters, unseed_counters),
    ]
