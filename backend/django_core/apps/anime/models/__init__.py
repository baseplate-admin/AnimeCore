from django_better_admin_arrayfield.models.fields import ArrayField
from dynamic_filenames import FilePattern

from django.contrib.postgres.indexes import GinIndex
from django.db import models

from ...characters.models import CharacterModel
from ...episodes.models import EpisodeModel
from ...producers.models import ProducerModel
from ...studios.models import StudioModel
from .anime_genre import AnimeGenreModel
from .anime_theme import AnimeThemeModel

anime_cover_upload_pattern = FilePattern(filename_pattern="/anime_cover/{uuid:s}{ext}")
anime_banner_upload_pattern = FilePattern(filename_patten="/anime_banner/{uuid:s}{ext}")

# Create your models here.


class AnimeModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=False, null=True)
    anilist_id = models.IntegerField(unique=True, blank=False, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=False, null=True)

    anime_name = models.CharField(unique=True, max_length=1024)
    anime_name_japanese = models.CharField(max_length=1024, null=True)
    anime_name_synonyms = ArrayField(
        models.CharField(max_length=1024), blank=True, null=True
    )

    anime_source = models.CharField(max_length=128, blank=True, null=True)
    anime_aired_from = models.DateTimeField(blank=True, null=True)
    anime_aired_to = models.DateTimeField(blank=True, null=True)
    anime_banner = models.ImageField(
        upload_to=anime_banner_upload_pattern, default=None, blank=True, null=True
    )
    anime_cover = models.ImageField(
        upload_to=anime_cover_upload_pattern, default=None, blank=True, null=True
    )
    anime_synopsis = models.TextField(blank=True, null=True)
    anime_background = models.TextField(blank=True, null=True)
    anime_rating = models.CharField(max_length=50, blank=True, null=True)

    anime_genres = models.ManyToManyField(AnimeGenreModel, blank=True)
    anime_themes = models.ManyToManyField(AnimeThemeModel, blank=True)
    anime_studios = models.ManyToManyField(StudioModel, blank=True)
    anime_producers = models.ManyToManyField(ProducerModel, blank=True)
    anime_characters = models.ManyToManyField(CharacterModel, blank=True)

    anime_recommendation = models.ManyToManyField("self", blank=True)
    anime_episodes = models.ManyToManyField(EpisodeModel, blank=True)

    updated = models.DateTimeField(auto_now_add=True)
    # anime_rating = models.CharField(max_length=128)

    def __str__(self) -> str:
        return f"{self.anime_name}"

    class Meta:
        verbose_name = "Anime"
        indexes = [
            # Index for 'anime_name' , 'anime_name_japanese', 'anime_name_synonyms'
            GinIndex(
                fields=[
                    "anime_name",
                    "anime_name_japanese",
                    "anime_name_synonyms",
                ],
            )
        ]
