from sqlalchemy import (Table,
                        Column,
                        Integer,
                        ForeignKey,
                        UniqueConstraint)
from .base import Base

tasks_tags_association_table = Table(
    "tasks_tags_association",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("task_id", Integer,
           ForeignKey("tasks.id"),
           nullable=False
           ),
    Column("tag_id", Integer,
           ForeignKey("tags.id"),
           nullable=False
           ),
    UniqueConstraint("task_id", "tag_id")
)
