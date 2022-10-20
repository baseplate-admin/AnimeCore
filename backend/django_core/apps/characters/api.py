from core.permissions import is_superuser
from ninja import Query, Router
from ninja.pagination import paginate

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .filters import CharacterFilter
from .models import CharacterModel
from .schemas import CharacterSchema

router = Router(tags=["characters"])


@router.get("", response=list[CharacterSchema])
@paginate
def get_character_info(
    request: HttpRequest,
    filters: CharacterFilter = Query(...),
) -> QuerySet[CharacterModel]:
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)
    query = CharacterModel.objects.all()

    character_name = query_dict.pop("name", None)
    if character_name:
        _vector_ = SearchVector("name", "about")
        _query_ = SearchQuery(character_name)
        query = query.annotate(
            character_rank=SearchRank(
                _vector_,
                _query_,
            )
        ).order_by("-character_rank")

    # Same here but with ids
    id_lookups = [
        "mal_id",
        "kitsu_id",
        "anilist_id",
    ]
    for id in id_lookups:
        value = query_dict.pop(id, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{id}": int(position.strip())})
            query_object &= _query_

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:character_id}/", response=CharacterSchema)
@login_required
@user_passes_test(is_superuser)
def get_individual_character_info(
    request: HttpRequest,
    character_id: str,
) -> QuerySet[CharacterModel]:
    queryset = get_object_or_404(CharacterModel, id=character_id)
    return queryset
