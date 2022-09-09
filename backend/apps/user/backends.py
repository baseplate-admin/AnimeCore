from typing import Any

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.http import HttpRequest

from apps.user.models import CustomUser


class EmailOrUsernameModelBackend(ModelBackend):
    """
    Authentication backend which allows users to authenticate using either their
    username or email address

    Source: https://stackoverflow.com/a/35836674/59984
    """

    def authenticate(
        self,
        request: HttpRequest | None,
        username: str | None = None,
        password: str | None = None,
        **kwargs: Any,
    ) -> CustomUser:
        user_model = get_user_model()
        query = Q()
        # So `username` is something like baseplate-admin#0001
        # we need to split to get the username and discriminator
        if username:
            try:
                _username_ = username.split("#")
                username = _username_[0]
                username_discriminator = _username_[1]
                query |= Q(username_discriminator=username_discriminator) & Q(
                    **{user_model.USERNAME_FIELD: username}
                )
            except IndexError:
                pass
            finally:
                if "@" in username:
                    query |= Q(email__iexact=username)

        # The `username` field is allows to contain `@` characters so
        # technically a given email address could be present in either field,
        # possibly even for different users, so we'll query for all matching
        # records and test each one.
        users = user_model._default_manager.filter(query)

        # Test whether any matched user has the provided password:
        for user in users:
            if user.check_password(password):
                return user

        if not users:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (see
            # https://code.djangoproject.com/ticket/20760)
            user_model().set_password(password)
