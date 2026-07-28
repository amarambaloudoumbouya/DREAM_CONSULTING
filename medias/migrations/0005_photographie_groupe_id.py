import uuid

from django.db import migrations, models


def regrouper_photos_existantes(apps, schema_editor):
    """Regroupe les photos créées quasi simultanément dans la même catégorie."""
    Photographie = apps.get_model('medias', 'Photographie')
    photos = list(Photographie.objects.order_by('created_at', 'id'))
    if not photos:
        return

    current_groupe = uuid.uuid4()
    prev = photos[0]
    prev.groupe_id = current_groupe
    prev.save(update_fields=['groupe_id'])

    for photo in photos[1:]:
        same_batch = (
            photo.categorie == prev.categorie
            and abs((photo.created_at - prev.created_at).total_seconds()) < 3
        )
        if not same_batch:
            current_groupe = uuid.uuid4()
        photo.groupe_id = current_groupe
        photo.save(update_fields=['groupe_id'])
        prev = photo


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0004_photographie_categorie_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='photographie',
            name='groupe_id',
            field=models.UUIDField(
                db_index=True,
                default=uuid.uuid4,
                editable=False,
                help_text='Identifiant partagé par les photos ajoutées en même temps.',
                verbose_name='Groupe',
            ),
        ),
        migrations.RunPython(regrouper_photos_existantes, migrations.RunPython.noop),
    ]
