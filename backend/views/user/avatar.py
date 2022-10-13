from fastapi import APIRouter, Depends
from models.user import User
from fastapi.responses import StreamingResponse, FileResponse
from fastapi import Request

router = APIRouter()


@router.get("/avatar/{user_id:str}")
async def get_avatar(request: Request, user_id: str | None = None):
    user_model: User = User.get(id=user_id)
    if user_model.avatar:
        response = FileResponse(user_model.avatar)
    else:
        response = web.StreamResponse()

        url = str(
            URL(
                user_model.avatar_provider.format(
                    EMAIL=hashlib.md5(
                        user_model.email.strip().lower().encode()
                    ).hexdigest()
                )
            ),
        )

        async with client_session.get(url, allow_redirects=True) as r:
            response.content_type = r.headers["content-type"]
            await response.prepare(request)

            async for line in r.content:
                await response.write(line)

    # Lets confuse peoples
    return response
