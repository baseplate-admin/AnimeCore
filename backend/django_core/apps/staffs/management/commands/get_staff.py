import sys
from argparse import ArgumentParser
from typing import Any

from django.core.files.images import ImageFile
from django.core.management.base import BaseCommand

from shinobi.parser.staff import StaffParser
from shinobi.utilities.session import session

from ...models import StaffAlternateNameModel, StaffModel
from ...tasks import get_periodic_staff


class Command(BaseCommand):
    help = "Django command that gets the Staff Information given mal_id"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self.client = session
        super().__init__(*args, **kwargs)

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "staff_id",
            type=int,
            help="The staff number to get information for",
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

    def handle(self, *args: Any, **options: dict[str, Any]) -> None:
        periodic: bool = bool(options["periodic"])
        if periodic:
            get_periodic_staff.delay()
            self.stdout.write("Successfully stated preiodic celery commands")
            sys.exit(0)

        staff_id: str = str(options["staff_id"])
        if not staff_id:
            self.stdout.write(self.style.ERROR("No staff_id provided"))
            sys.exit(1)

        create: bool = bool(options["create"])
        if create:
            staff_instance, _ = StaffModel.objects.get_or_create(mal_id=staff_id)

        else:
            try:
                staff_instance = StaffModel.objects.get(mal_id=staff_id)

            except StaffModel.DoesNotExist:
                self.stdout.write(f"No StaffModel found for {self.style.ERROR(staff_id)}")
                sys.exit(1)

        res = self.client.get(f"https://myanimelist.net/people/{staff_id}")

        parser = StaffParser(res.text)
        data_dictionary = {k: v for k, v in parser.build_dictionary().items() if v}

        if alternate_name := data_dictionary.pop("alternate_name"):
            for name in alternate_name:
                instance, created = StaffAlternateNameModel.objects.get_or_create(name)
                if created:
                    StaffModel.alternate_names.add(instance)

        for attr, value in data_dictionary.items():
            if attr == "staff_image":
                setattr(
                    staff_instance,
                    attr,
                    ImageFile(
                        value["image"],
                        name=f"{staff_id}.{value['mimetype'].lower()}",
                    ),
                )

            else:
                setattr(staff_instance, attr, value)

        staff_instance.save()

        self.stdout.write(f"Successfully got info for {self.style.SUCCESS(staff_id)}")
