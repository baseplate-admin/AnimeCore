import asyncio
import httpx
import os
import dotenv

dotenv.load_dotenv()

STREAMSB_API_BASE_URL = "https://api.streamsb.com/api"
STREAMSB_API_KEY = os.getenv("STREAMSB_API_KEY")


async def get_streamsb_file_status(file_code: str):
    async with httpx.AsyncClient() as client:
        params = {"key": STREAMSB_API_KEY, "file_code": file_code}
        response = await client.get(
            f"{STREAMSB_API_BASE_URL}/file/url_uploads", params=params
        )
        return response.json()


async def upload_to_streamsb_by_url(url: str):
    async with httpx.AsyncClient() as client:
        params = {"key": STREAMSB_API_KEY, "url": url}
        response = await client.get(f"{STREAMSB_API_BASE_URL}/upload/url", params=params)
        return response.json()["result"]["filecode"]


async def upload_to_streamsb_by_file(file_path: str) -> str:
    async with httpx.AsyncClient() as client:
        with open(file_path, "rb") as file:
            params = {"key": STREAMSB_API_KEY}
            response = await client.get(
                f"{STREAMSB_API_BASE_URL}/upload/server", params=params
            )
            response.raise_for_status()
            upload_server = response.json()["result"]

            data = {"api_key": STREAMSB_API_KEY, "json": "1"}
            files = {"file": file}
            response = await client.post(upload_server, files=files, data=data)
            response.raise_for_status()
            return response.json()["result"]


# # Examples :
# async def main():
#     result = await upload_to_streamsb_by_file(
#         "death_note-01.mp4"
#     )  # return uploaded file_code and status
#     print(result)
#     # filecode = await upload_to_streamsb_by_url("https://bokunopico.mp4")

#     # status = await get_streamsb_file_status("bokunopico")


# if __name__ == "__main__":
#     asyncio.run(main())
