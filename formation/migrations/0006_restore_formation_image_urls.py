from django.db import migrations


IMAGE_URLS = {
    'photographie': 'front/assets/img/gallery/1.jpg',
    'videographie': 'front/assets/img/gallery/2.jpg',
    'design-branding': 'front/assets/img/gallery/3.jpg',
    'motion-design': 'front/assets/img/gallery/4.jpg',
    'drone': 'front/assets/img/gallery/5.jpg',
}


def restore_image_urls(apps, schema_editor):
    Formation = apps.get_model('formation', 'Formation')
    for slug, path in IMAGE_URLS.items():
        Formation.objects.filter(slug=slug).update(image_url=path)


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0005_formation_image_url'),
    ]

    operations = [
        migrations.RunPython(restore_image_urls, migrations.RunPython.noop),
    ]
