# Generated by Django 4.0.3 on 2022-03-26 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("upload", "0042_alter_episodecommentmodel_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="episodemodel",
            name="episode_timestamps",
            field=models.ManyToManyField(blank=True, to="upload.episodetimestampmodel"),
        ),
    ]
