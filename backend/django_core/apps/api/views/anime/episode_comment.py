from apps.anime.models import AnimeModel
from apps.episodes.models.episode_comment import EpisodeCommentModel
from ninja import Router

from django.http import HttpRequest
from django.shortcuts import get_list_or_404, get_object_or_404

from ...schemas.episodes.episode_comment import (
    EpisodeCommentTreeGETSchema,
)
from ...decorator import recursionlimit

router = Router()


@recursionlimit(90000)
def get_nested_children(item: EpisodeCommentModel):
    _list = []
    _list.append(
        {
            "pk": item.pk,
            "user": str(item.user),
            "text": item.text,
            "comment_added": item.comment_added,
            "children": [get_nested_children(i)[0] for i in item.get_children()],
        }
    )
    return _list


@router.get(
    "/{int:anime_id}/episodes/{int:episode_number}/comments",
    response=list[EpisodeCommentTreeGETSchema],
)
def get_individual_anime_episode_comments(
    request: HttpRequest,
    anime_id: int,
    episode_number: int,
):
    query: list[EpisodeCommentModel] = get_list_or_404(
        get_object_or_404(
            AnimeModel,
            pk=anime_id,
        )
        .episodes.get(episode_number=episode_number)
        .episode_comments.all()
    )

    return_list = []

    while query:
        item = query.pop()
        return_list.extend(get_nested_children(item))

    return return_list
