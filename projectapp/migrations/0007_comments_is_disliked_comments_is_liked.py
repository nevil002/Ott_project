# Generated by Django 4.2.6 on 2023-12-12 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectapp', '0006_comments_dislike_comments_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='is_disliked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='comments',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]