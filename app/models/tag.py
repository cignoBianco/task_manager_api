from sqlalchemy import Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from ..core.config.database import Base
from .associations import task_tags
from .base import UUIDMixin

class Tag(UUIDMixin, Base):
    __tablename__ = "tags"

    name = Column(String, unique=True, nullable=False)

    tasks = relationship("Task", secondary=task_tags, back_populates="tags")
