# Generated by Django 4.2.6 on 2023-12-11 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_genre_remove_movies_genre_movies_genre_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='dislike',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movies',
            name='like',
            field=models.IntegerField(default=0),
        ),
    ]
