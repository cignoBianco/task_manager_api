from sqlalchemy import Column, Integer, String, Text
from ..core.config.database import Base
from .base import UUIDMixin

class UserRole(UUIDMixin, Base):
    __tablename__ = "user_roles"

    role_name = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
