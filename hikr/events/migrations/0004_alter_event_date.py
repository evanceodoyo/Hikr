# Generated by Django 4.2.4 on 2023-09-04 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_date_alter_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 9, 11, 17, 21, 48, 329555)),
        ),
    ]
