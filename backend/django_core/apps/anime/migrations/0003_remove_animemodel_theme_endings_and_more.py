# Generated by Django 4.1.7 on 2023-03-15 05:35

import dynamic_filenames

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("anime", "0002_animemodel_staffs_alter_animemodel_rating"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="animemodel",
            name="theme_endings",
        ),
        migrations.RemoveField(
            model_name="animemodel",
            name="theme_openings",
        ),
        migrations.CreateModel(
            name="AnimeOpeningModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entry", models.BigIntegerField()),
                ("name", models.CharField(max_length=512)),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="opening/{uuid:s}{ext}"
                        ),
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("entry", "name")},
            },
        ),
        migrations.CreateModel(
            name="AnimeEndingModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("entry", models.BigIntegerField()),
                ("name", models.CharField(max_length=512)),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="ending/{uuid:s}{ext}"
                        ),
                    ),
                ),
            ],
            options={
                "abstract": False,
                "unique_together": {("entry", "name")},
            },
        ),
        migrations.AddField(
            model_name="animemodel",
            name="endings",
            field=models.ManyToManyField(blank=True, to="anime.animeendingmodel"),
        ),
        migrations.AddField(
            model_name="animemodel",
            name="openings",
            field=models.ManyToManyField(blank=True, to="anime.animeopeningmodel"),
        ),
    ]
