import sys
import time
from typing import NoReturn

from shinobi.parser.character import CharacterParser
from shinobi.utilities.session import session

from django.core.management.base import BaseCommand

from ...models import CharacterModel
from ...tasks import get_perodic_character

TIMEOUT = 2


class Command(BaseCommand):
    help = "Django command that gets the Character Information given mal_id"

    def __init__(self, *args, **kwargs) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser):
        parser.add_argument(
            "character_id",
            type=int,
            help="The character number to get information for",
            nargs="?",
        )
        parser.add_argument(
            "--create",
            action="store_true",
            help="Flag to indicate that the anime will be created",
        )
        parser.add_argument(
            "--periodic",
            action="store_true",
            help="Flag to periodic task will be created",
        )

    def handle(self, *args, **options) -> NoReturn:
        character_id: int = options["character_id"]
        create: bool = options["create"]
        periodic: bool = options["periodic"]

        if periodic:
            get_perodic_character.delay()
            self.stdout.write(f"Successfully stated preiodic celery commands")
            sys.exit(0)

        res = self.client.get(f"https://myanimelist.net/character/{character_id}")

        parser = CharacterParser(res.text)
        data_dictionary = parser.build_dictionary()

        if create:
            character_instance, _ = CharacterModel.objects.get_or_create(
                mal_id=character_id
            )

        try:
            character_instance = CharacterModel.objects.get(mal_id=character_id)
        except CharacterModel.DoesNotExist:
            self.stdout.write(
                f"No CharacterModel found for {self.style.ERROR(character_id)}"
            )
            sys.exit(1)

        for attr, value in data_dictionary.items():
            if value:
                setattr(character_instance, attr, value)

        character_instance.save()
        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(character_id)}")
