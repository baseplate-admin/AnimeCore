from ..input.episode import EpisodeInput
import strawberry
import strawberry_django
from ..permissions import IsSuperUser
from strawberry import Info
from apps.gql.functions.dictionary import clean_dictionary
from apps.episodes.models import EpisodeModel
from typing import cast
from ..types.episode import EpisodeType


@strawberry.type
class EpisodeMutation:
    @strawberry_django.mutation(
        permission_classes=[IsSuperUser],
        extensions=[strawberry_django.permissions.IsSuperuser()],
    )
    def add_episode(self, info: Info, data: EpisodeInput) -> EpisodeType:
        kwargs = {
            "episode_number": data.episode_number,
            "episode_name": data.episode_name,
            "episode_summary": data.episode_summary,
            "episode_length": data.episode_length,
            "episode_type": data.episode_type,
            # 'episode_timestamps': "",
            # "providers": data.providers,
        }
        model_data = clean_dictionary(dictionary=kwargs)

        instance = EpisodeModel.objects.create(**model_data)

        return cast(EpisodeType, instance)
