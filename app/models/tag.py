from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from ..core.config.database import Base
from .task import task_tags
from .base import UUIDMixin

class Tag(UUIDMixin, Base):
    __tablename__ = "tags"

    name = Column(String, unique=True, nullable=False)

    tasks = relationship("Task", secondary=task_tags, back_populates="tags")


# class TaskTag(Base):
#     __tablename__ = "task_tags"

#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"))
#     tag = Column(String(100), nullable=False)
