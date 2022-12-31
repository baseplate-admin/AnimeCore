from apps.anime.models import AnimeModel
from apps.studios.models import StudioModel
from core.permissions import is_superuser
from ninja import Router

from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.studios import StudioSchema

router = Router()


@router.get("/{int:anime_id}/studios", response=list[StudioSchema])
def get_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
) -> list[StudioModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, id=anime_id).anime_studios,
    )

    return query


@router.post("/{int:anime_id}/studios", response=StudioSchema)
@login_required
@user_passes_test(is_superuser)
def post_individual_anime_studio_info(
    request: HttpRequest,
    anime_id: int,
    payload: StudioSchema,
) -> StudioModel:
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = StudioModel.objects.get_or_create(
        **payload.dict(),
    )

    instance: StudioModel = query[0]
    anime_info_model.anime_studios.add(instance)

    return instance
