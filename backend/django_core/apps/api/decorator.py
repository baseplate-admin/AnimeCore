import sys
from collections.abc import Callable
from functools import wraps
from http import HTTPStatus
from typing import TYPE_CHECKING, Any

from apps.user.models import CustomUser
from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest
from ninja.errors import HttpError

if TYPE_CHECKING:
    from .permissions import IsSuperUser


def recursionlimit(limit: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            old_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(limit)
            try:
                result = func(*args, **kwargs)
            finally:
                sys.setrecursionlimit(old_limit)
            return result

        return wrapper

    return decorator


# The following decorators were inspired by this comment
# https://github.com/vitalik/django-ninja/discussions/580#discussioncomment-3795237


def throttle():
    def decorator(func):
        @wraps(func)
        def wrapper(request: HttpRequest, *args, **kwargs):
            if False:
                return 429, None
            return func(request, *args, **kwargs)

        return wrapper

    return decorator


def permission_required(
    permissions: list[Callable[[HttpRequest, CustomUser], "IsSuperUser"]],
    key: str | None = "auth",  # To get request.auth
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(request: HttpRequest, *args: Any, **kwargs: Any) -> Any:
            user = getattr(request, key, AnonymousUser)

            permission_granted = any(
                [permission(request, user).has_permissions() for permission in permissions]
            )
            if not permission_granted:
                raise HttpError(
                    HTTPStatus.UNAUTHORIZED,
                    "Superuser is required for this operation",
                )
            return func(request, *args, **kwargs)

        return wrapper

    return decorator
