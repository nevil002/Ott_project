# Generated by Django 4.2.6 on 2023-11-23 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('genre', models.CharField(default=False, max_length=15)),
                ('year', models.IntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
    ]
