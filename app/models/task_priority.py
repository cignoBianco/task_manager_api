from sqlalchemy import Column, Integer, String
from ..core.config.database import Base
from .base import UUIDMixin


class TaskPriority(UUIDMixin, Base):
    __tablename__ = "task_priorities"

    priority_name = Column(String(20), unique=True, nullable=False)
    weight = Column(Integer, default=0)
    color = Column(String(7), default="#FFFFFF")
