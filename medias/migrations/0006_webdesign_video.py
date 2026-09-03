# Generated manually for WebDesign image -> video

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0005_photographie_groupe_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='webdesign',
            name='image',
        ),
        migrations.RemoveField(
            model_name='webdesign',
            name='image_statique',
        ),
        migrations.AddField(
            model_name='webdesign',
            name='video',
            field=models.FileField(
                blank=True,
                help_text='Aperçu vidéo du projet (MP4). Si vide, la vidéo de secours est utilisée.',
                upload_to='medias/web_design/',
                verbose_name='Vidéo',
            ),
        ),
        migrations.AddField(
            model_name='webdesign',
            name='video_statique',
            field=models.CharField(
                blank=True,
                help_text='Ex. front/assets/video/hero-video.mp4',
                max_length=255,
                verbose_name='Vidéo static (secours)',
            ),
        ),
    ]
