# Generated by Django 4.0.3 on 2022-03-16 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0014_rename_episode_number_episodemodel_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="episodemodel",
            name="episode_number",
            field=models.BigIntegerField(default=0),
        ),
    ]
