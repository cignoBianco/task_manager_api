from sqlalchemy import Column, String, TIMESTAMP, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from ..core.config.database import Base
from .base import UUIDMixin

class User(UUIDMixin, Base):
    __tablename__ = "users"

    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    role_id = Column(UUID(as_uuid=True), ForeignKey("user_roles.id"), nullable=True)

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
    updated_at = Column(TIMESTAMP(timezone=True), server_default=func.now(), onupdate=func.now())

    role = relationship("UserRole")
