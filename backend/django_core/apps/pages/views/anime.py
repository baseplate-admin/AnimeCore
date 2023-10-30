from typing import TYPE_CHECKING

from django.http import HttpResponse
from django.shortcuts import render

from ..data.anime import icons, latest_animes

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest


async def anime_home_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        return render(request, "anime/_partial.html")

    return render(
        request,
        "anime/home.html",
        context={"icons": icons, "latest_animes": latest_animes},
    )
