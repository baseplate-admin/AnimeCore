from http import HTTPStatus
from apps.anime.models import AnimeModel
from apps.characters.models import CharacterModel
from ninja import Router

from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404

from apps.user.models import CustomUser
from apps.api.auth import AuthBearer

from ...schemas.characters import CharacterSchema

router = Router()


@router.get("/{int:anime_id}/character", response=list[CharacterSchema])
def get_individual_anime_character_info(
    request: HttpRequest,
    anime_id: int,
) -> list[CharacterModel]:
    query = get_list_or_404(
        get_object_or_404(AnimeModel, pk=anime_id).characters,
    )
    return query


@router.post(
    "/{int:anime_id}/character",
    response=list[CharacterSchema],
    auth=AuthBearer(),
)
def post_individual_anime_character_info(
    request: HttpRequest,
    anime_id: int,
    payload: CharacterSchema,
) -> CharacterModel:
    user: CustomUser = request.auth
    if not user.is_superuser:
        raise HttpResponse(
            "Superuser is required for this operation",
            status_code=HTTPStatus.UNAUTHORIZED,
        )
    # Set this at top
    # Because if there is no anime_info_model with corresponding query
    # theres no point in continuing
    anime_info_model = get_object_or_404(AnimeModel, pk=anime_id)

    query = CharacterModel.objects.get_or_create(
        **payload.dict(),
    )
    instance: CharacterModel = query[0]
    anime_info_model.characters.add(instance)

    return instance
