from ninja import Query, Router
from ninja.pagination import paginate

from django.db.models import Q, QuerySet
from django.http import HttpRequest
from django.shortcuts import get_object_or_404

from .filters import StaffFilter
from .models import StaffModel
from .schemas import StaffSchema

router = Router(tags=["staffs"])


@router.get("", response=list[StaffSchema])
@paginate
def get_staff_info(
    request: HttpRequest,
    filters: StaffFilter = Query(...),
) -> QuerySet[StaffModel]:
    query_object = Q()
    query_dict = filters.dict(exclude_none=True)

    staff_name = query_dict.pop("name", None)
    if staff_name:
        _query_ = Q()
        # Modify this
        for position in staff_name.split(","):
            _query_ |= Q(**{"name__icontains": position.strip()}) | Q(
                **{"alternate_names__name__icontains": position.strip()}
            )
        query_object &= _query_

    # Specilized lookups
    specialized_name_lookups = [
        "given_name",
        "family_name",
    ]
    for specialized_name in specialized_name_lookups:
        value = query_dict.pop(specialized_name, None)
        if value:
            _query_ = Q()
            for position in value.split(","):
                _query_ |= Q(**{f"{specialized_name}__icontains": int(position.strip())})
            query_object &= _query_

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

    query = StaffModel.objects.all()

    if query_object:
        query = query.filter(query_object).distinct()

    return query


@router.get("/{str:staff_id}/", response=StaffSchema)
def get_individual_staff_info(
    request: HttpRequest,
    staff_id: str,
):
    queryset = get_object_or_404(StaffModel, id=staff_id)
    return queryset
