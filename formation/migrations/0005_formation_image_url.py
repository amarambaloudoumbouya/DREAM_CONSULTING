from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0004_inscription_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='image_url',
            field=models.CharField(
                blank=True,
                help_text='Ex: front/assets/img/gallery/1.jpg',
                max_length=255,
                verbose_name='Image de la formation URL',
            ),
        ),
    ]
