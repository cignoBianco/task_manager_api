import uuid
from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP, Interval
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from ..core.config.database import Base
from .base import UUIDMixin


class MLPrediction(UUIDMixin, Base):
    __tablename__ = "ml_predictions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    task_id = Column(UUID(as_uuid=True), ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)

    priority_id = Column(UUID(as_uuid=True), ForeignKey("task_priorities.id"))

    predicted_duration = Column(Interval)

    assignment_recommendation = Column(JSONB)
    risk_level = Column(String(20))
    model_version = Column(String(50))

    created_at = Column(TIMESTAMP(timezone=True), server_default=func.now())
