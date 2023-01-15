# Generated by Django 4.2 on 2023-01-15 03:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AnilistModel",
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
                ("access_token", models.CharField(blank=True, max_length=64, null=True)),
                ("expires_in", models.DurationField(blank=True, null=True)),
                ("refresh_token", models.CharField(blank=True, max_length=64, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "AniList",
                "verbose_name_plural": "AniList",
            },
        ),
        migrations.CreateModel(
            name="KitsuModel",
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
                ("access_token", models.CharField(blank=True, max_length=64, null=True)),
                ("expires_in", models.DurationField(blank=True, null=True)),
                ("refresh_token", models.CharField(blank=True, max_length=64, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Kitsu",
                "verbose_name_plural": "Kitsu",
            },
        ),
        migrations.CreateModel(
            name="MalModel",
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
                ("access_token", models.CharField(blank=True, max_length=1024, null=True)),
                ("expires_in", models.DurationField(blank=True, null=True)),
                ("refresh_token", models.CharField(blank=True, max_length=1024, null=True)),
                ("created_at", models.DateTimeField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "MyAnimeList",
                "verbose_name_plural": "MyAnimeList",
            },
        ),
    ]
