from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from ..core.config.database import Base

task_tags = Table(
    "task_tags",
    Base.metadata,
    Column("task_id", UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), primary_key=True),
    Column("tag_id", UUID(as_uuid=True), ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True),
)
