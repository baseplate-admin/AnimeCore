from http import HTTPStatus

from apps.anime.models.anime_genre import AnimeGenreModel
from apps.api.auth import AuthBearer
from apps.user.models import CustomUser
from ninja import Router, Query

from django.http import HttpRequest, HttpResponse
from ...filters.genres import GenreFilter
from ...schemas.anime.anime_genre import AnimeGenreGETSchema, AnimeGenrePOSTSchema

router = Router()


@router.get("/genres", response=list[AnimeGenreGETSchema])
def get_anime_genre_info(
    request: HttpRequest,
    filters: GenreFilter = Query(...),
) -> list[AnimeGenreModel]:
    query = AnimeGenreModel.objects.filter(
        type__icontains="anime", **filters.dict(exclude_none=True)
    )

    return query


@router.post("/genres", response=list[AnimeGenreGETSchema], auth=AuthBearer())
def post_anime_genre_info(
    request: HttpRequest,
    payload: list[AnimeGenrePOSTSchema],
) -> list[AnimeGenreModel]:
    user: CustomUser = request.auth
    if not user.is_superuser:
        return HttpResponse(
            "Superuser is required for this operation", status=HTTPStatus.UNAUTHORIZED
        )

    instance_objects = []
    for object in payload:
        instance_objects.append(
            AnimeGenreModel(
                type="anime",
                **object.dict(exclude_none=True),
            )
        )

    query = AnimeGenreModel.objects.bulk_create(instance_objects)
    print(query)
    return query
