# Generated by Django 4.2.4 on 2023-09-04 14:21

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_groupmembership_is_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='groups/images/default.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[768, 1024], upload_to='groups/images'),
        ),
    ]
