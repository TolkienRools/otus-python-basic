from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, ForeignKey
from .base import Base
from .tasks_tags_association import tasks_tags_association_table

if TYPE_CHECKING:
    from .tag import Tag


class Task(Base):

    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str]
    published_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=False))

    tags: Mapped[list["Tag"]] = relationship(
        secondary=tasks_tags_association_table,
        back_populates="tasks",
        order_by="Tag.id"
    )

    @property
    def tags_names(self):
        return [tag.name for tag in self.tags]

    @property
    def tags_str(self):
        return ",".join(self.tags_names)
