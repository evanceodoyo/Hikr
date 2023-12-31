# Generated by Django 4.2.4 on 2023-08-24 14:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
                ('date', models.DateField(default=datetime.datetime(2023, 8, 31, 17, 6, 19, 610308))),
                ('time', models.TimeField(default=datetime.time(8, 0))),
                ('difficulty', models.CharField(choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced')], default='beginner', max_length=12)),
                ('image', django_resized.forms.ResizedImageField(crop=None, default='events/images/default.png', force_format='JPEG', keep_meta=True, quality=75, scale=0.5, size=[400, 500], upload_to='events/images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organized_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'events',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='EventAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendees', to='events.event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'event_attendance',
                'ordering': ['-joined_at'],
                'unique_together': {('user', 'event')},
            },
        ),
    ]
