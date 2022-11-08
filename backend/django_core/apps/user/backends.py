from typing import Any

from apps.user.models import CustomUser

from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpRequest


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address

    Source: https://stackoverflow.com/a/35836674/59984
    """

    def authenticate(
        self,
        request: HttpRequest,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> CustomUser | None:
        # So `username` is something like baseplate-admin#0001
        # we need to split to get the username and discriminator

        try:
            user: CustomUser = CustomUser.objects.get_username_with_discriminator().get(
                Q(username_with_discriminator=username) | Q(email__iexact=username)
            )

            if user.check_password(password):
                query = user

        except CustomUser.DoesNotExist:
            query = None

        finally:
            return query
