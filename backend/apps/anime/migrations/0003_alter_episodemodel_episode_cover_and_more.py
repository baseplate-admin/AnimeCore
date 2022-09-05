# Generated by Django 4.1.1 on 2022-09-05 13:41

from django.db import migrations, models

import apps.anime.models.episode
import core.storages


class Migration(migrations.Migration):

    dependencies = [
        ("anime", "0002_delete_charactermodel_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episodemodel",
            name="episode_cover",
            field=models.ImageField(
                blank=True,
                default=None,
                null=True,
                storage=core.storages.OverwriteStorage(),
                upload_to=apps.anime.models.episode.FileField.episode_cover,
            ),
        ),
        migrations.AlterField(
            model_name="episodemodel",
            name="episode_file",
            field=models.FileField(
                blank=True,
                default=None,
                null=True,
                storage=core.storages.OverwriteStorage(),
                upload_to=apps.anime.models.episode.FileField.episode_upload,
            ),
        ),
    ]
