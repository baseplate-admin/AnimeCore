# Generated by Django 4.2 on 2023-01-15 03:14

import core.storages
import dynamic_filenames

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="StaffModel",
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
                ("mal_id", models.IntegerField(blank=True, null=True, unique=True)),
                ("kitsu_id", models.IntegerField(blank=True, null=True, unique=True)),
                ("anilist_id", models.IntegerField(blank=True, null=True, unique=True)),
                ("name", models.CharField(max_length=1024)),
                ("given_name", models.CharField(blank=True, max_length=1024, null=True)),
                ("family_name", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "staff_image",
                    models.ImageField(
                        blank=True,
                        default=None,
                        null=True,
                        storage=core.storages.OverwriteStorage,
                        upload_to=dynamic_filenames.FilePattern(
                            filename_pattern="staffs/{uuid:s}{ext}"
                        ),
                    ),
                ),
                ("about", models.TextField(blank=True, null=True)),
                (
                    "alternate_names",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.CharField(max_length=1024),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff | People",
                "verbose_name_plural": "Staffs | Peoples",
            },
        ),
    ]
