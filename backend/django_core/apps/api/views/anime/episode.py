from apps.anime.models import AnimeModel
from apps.episodes.models import EpisodeModel
from core.permissions import is_superuser
from ninja import Router

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.episodes import EpisodeGETSchema, EpisodePOSTSchema

router = Router()


@router.get("/{int:anime_id}/episodes", response=list[EpisodeGETSchema])
def get_individual_anime_episodes(
    request: HttpRequest,
    anime_id: int,
) -> list[EpisodeModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, id=anime_id).anime_episodes,
    )
    return query


# I will work on this
# File upload is broken
# https://github.com/vitalik/django-ninja/issues/371
# https://django-ninja.rest-framework.com/tutorial/file-params/
@router.post("/{int:anime_id}/episodes", response=EpisodeGETSchema)
@login_required
@user_passes_test(is_superuser)
def post_individual_anime_episodes(
    request: HttpRequest,
    anime_id: int,
    payload: EpisodePOSTSchema,
) -> EpisodeModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)
    query = EpisodeModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: EpisodeModel = query[0]
    anime_info_model.anime_studios.add(instance)

    return instance
