# Generated by Django 4.2.6 on 2023-11-24 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_movies_poster_movies_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='Video',
            new_name='File',
        ),
    ]