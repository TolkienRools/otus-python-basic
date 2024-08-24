"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import Sequence, List
from jsonplaceholder_requests import (
    fetch_users_data,
    fetch_posts_data
)
from models import (
    Base,
    User,
    Post,
    async_engine,
    Session
)


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def create_users(
        session: Session,
        users_data: List[dict]
) -> Sequence[User]:
    users = [User(
        name=user_data["name"],
        username=user_data["username"],
        email=user_data["email"]
    ) for user_data in users_data]

    session.add_all(users)
    await session.commit()
    for user in users:
        await session.refresh(user)
    return users


async def create_posts(
        session: Session,
        user_id: int,
        posts_data: List[dict]
) -> Sequence[Post]:
    posts = [Post(
        title=post_data["title"],
        body=post_data["body"],
        user_id=user_id
    ) for post_data in posts_data]

    session.add_all(posts)
    await session.commit()
    for post in posts:
        await session.refresh(post)
    return posts


async def async_main():
    await create_tables()
    users_data: List[dict]
    posts_data: List[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    posts_offset = len(posts_data) // len(users_data)

    async with Session() as session:
        users = await create_users(session, users_data)
        offset = 0
        for user in users:
            await create_posts(session, user.id, posts_data[offset:offset + posts_offset])
            offset += posts_offset


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
