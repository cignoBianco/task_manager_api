from sqlalchemy import Column, Integer, String, Text
from ..core.config.database import Base
from .base import UUIDMixin

class ProjectStatus(UUIDMixin, Base):
    __tablename__ = "project_statuses"

    status_name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    color = Column(String(7), default="#FFFFFF")
