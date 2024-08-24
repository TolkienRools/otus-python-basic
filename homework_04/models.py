"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    declared_attr
)
from sqlalchemy import (
    String,
    ForeignKey
)

PG_CONN_URI = (os.environ.get("SQLALCHEMY_PG_CONN_URI") or
               "postgresql+asyncpg://postgres:password@localhost/postgres")

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=False
)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"


Session = async_sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)



class User(Base):
    name: Mapped[str] = mapped_column(String(32), nullable=False, default="")
    username: Mapped[str] = mapped_column(String(32), nullable=False, unique=True)
    email: Mapped[str | None] = mapped_column(unique=True)

    posts: Mapped[list["Post"]] = relationship(back_populates="user")


class Post(Base):
    title: Mapped[str] = mapped_column(nullable=False, default="")
    body: Mapped[str] = mapped_column(nullable=False, default="")
    user_id: Mapped[str | None] = mapped_column(ForeignKey('users.id'))

    user: Mapped["User"] = relationship(back_populates="posts")
