from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from .base import Base
from .tasks_tags_association import tasks_tags_association_table

if TYPE_CHECKING:
    from .task import Task


class Tag(Base):

    name: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    tasks: Mapped[list["Task"]] = relationship(
        secondary=tasks_tags_association_table,
        back_populates="tags",
        order_by="Task.id"
    )

    def __repr__(self):
        return str(self)

    def __str__(self):
        return (f"{self.__class__.__name__}"
                f"id = {self.id}, "
                f"title = {self.name!r}"
                )


print("inited posts")
