import uuid
from sqlalchemy import Column, String, Text, Date, TIMESTAMP, Integer, ForeignKey, Interval, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from ..core.config.database import Base
from .task_status import TaskStatus
from .task_priority import TaskPriority
from .base import UUIDMixin
from .associations import task_tags


class Task(UUIDMixin, Base):
    __tablename__ = "tasks"

    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)

    title = Column(String(255), nullable=False)
    description = Column(Text)

    assignee_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))

    start_date = Column(Date)
    due_date = Column(Date)
    actual_end_date = Column(Date)

    status_id = Column(UUID(as_uuid=True), ForeignKey("task_statuses.id"))
    priority_id = Column(UUID(as_uuid=True), ForeignKey("task_priorities.id"))

    predicted_duration = Column(Interval)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    project = relationship("Project")
    assignee = relationship("User")
    status = relationship(TaskStatus)
    priority = relationship(TaskPriority)

    tags = relationship("Tag", secondary=task_tags, back_populates="tasks")


