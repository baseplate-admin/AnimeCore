from typing import Any

from apps.user.models import CustomUser

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import HttpRequest


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address

    Source: https://stackoverflow.com/a/35836674/59984
    """

    @staticmethod
    def get_user_given_username_and_password(
        username_or_email: str, password: str
    ) -> CustomUser:
        user_model = CustomUser
        # So `username` is something like baseplate-admin#0001
        # we need to split to get the username and discriminator
        try:
            user_model = user_model.objects.get_username_with_discriminator().get(
                Q(username_with_discriminator=username_or_email)
                | Q(email__iexact=username_or_email)
            )
            if check_password(password, user_model.password):
                query = user_model

        except CustomUser.DoesNotExist:
            query = None

        finally:
            return query

    def authenticate(
        self,
        request: HttpRequest | None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> CustomUser | None:
        return self.get_user_given_username_and_password(username, password)
