from pydantic import BaseModel
from uuid import UUID
from typing import Optional, Dict

class MLPredictionBase(BaseModel):
    task_id: UUID
    priority_id: Optional[int] = None
    predicted_duration: Optional[str] = None
    assignment_recommendation: Optional[Dict] = None
    risk_level: Optional[str] = None
    model_version: Optional[str] = None

class MLPredictionCreate(MLPredictionBase):
    pass

class MLPredictionRead(MLPredictionBase):
    id: UUID

    class Config:
        orm_mode = True
