import uuid

from django.db import migrations, models
from django.utils.text import slugify


def populate_slugs(apps, schema_editor):
    Inscription = apps.get_model('formation', 'Inscription')
    for inscription in Inscription.objects.all():
        base = slugify(f'{inscription.prenom} {inscription.nom}'.strip()) or slugify(inscription.email) or 'inscription'
        inscription.slug = f'{base}-{uuid.uuid4().hex[:5]}'
        inscription.save(update_fields=['slug'])


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0003_imagefield_and_prenom'),
    ]

    operations = [
        migrations.AddField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=255, null=True),
        ),
        migrations.RunPython(populate_slugs, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='inscription',
            name='slug',
            field=models.SlugField(editable=False, max_length=255, unique=True),
        ),
    ]
