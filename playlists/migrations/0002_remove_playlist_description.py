# Generated by Django 5.1.7 on 2025-03-31 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='description',
        ),
    ]
