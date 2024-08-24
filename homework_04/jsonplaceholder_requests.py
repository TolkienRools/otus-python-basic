from aiohttp import ClientSession
from typing import List

"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_url_data_json(url: str) -> List[dict]:
    async with ClientSession() as session:
        async with session.get(url) as result:
            return await result.json()


async def fetch_users_data() -> List[dict]:
    return await fetch_url_data_json(USERS_DATA_URL)


async def fetch_posts_data() -> List[dict]:
    return await fetch_url_data_json(POSTS_DATA_URL)
