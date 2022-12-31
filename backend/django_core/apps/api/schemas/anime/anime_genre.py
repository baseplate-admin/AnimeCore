from apps.anime.models import AnimeGenreModel
from ninja import ModelSchema


class AnimeGenreSchema(ModelSchema):
    class Config:
        model = AnimeGenreModel
        model_fields = "__all__"
