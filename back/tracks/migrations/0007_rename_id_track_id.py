# Generated by Django 4.0.5 on 2022-06-22 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0006_remove_track_id_track_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='track',
            old_name='id',
            new_name='ID',
        ),
    ]
