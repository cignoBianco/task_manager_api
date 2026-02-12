import uuid
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from ..core.config.database import Base
from .base import UUIDMixin


class TaskDependency(UUIDMixin, Base):
    __tablename__ = "task_dependencies"

    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)

    depends_on_task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id"), nullable=False)
