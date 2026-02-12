from sqlalchemy import Column, String, Text, Date, TIMESTAMP, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import uuid
from .project_status import ProjectStatus
from ..core.config.database import Base
from .base import UUIDMixin

class Project(UUIDMixin, Base):
    __tablename__ = "projects"

    name = Column(String(255), nullable=False)
    description = Column(Text)

    start_date = Column(Date)
    end_date = Column(Date)

    status_id = Column(UUID(as_uuid=True), ForeignKey("project_statuses.id"))
    manager_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    manager = relationship("User")
    status = relationship(ProjectStatus)
