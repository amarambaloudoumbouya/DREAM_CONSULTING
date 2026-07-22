import uuid

from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    DemandeDevis = apps.get_model('devis', 'DemandeDevis')
    for demande in DemandeDevis.objects.all():
        base = slugify(demande.nom_complet) or 'demande'
        demande.slug = f'{base}-{uuid.uuid4().hex[:5]}'
        demande.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('devis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demandedevis',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='demandedevis',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
