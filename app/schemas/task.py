from pydantic import BaseModel, ConfigDict
from typing import Optional, List
from uuid import UUID
from datetime import date, datetime
from .tag import TagRead

class TaskBase(BaseModel):
    project_id: UUID
    title: str
    description: Optional[str] = None
    assignee_id: Optional[UUID] = None
    start_date: Optional[date] = None
    due_date: Optional[date] = None
    actual_end_date: Optional[date] = None
    status_id: Optional[UUID] = None
    priority_id: Optional[UUID] = None
    tags: List[UUID] = []

class TaskCreate(TaskBase):
    tags: list[str] = []

class TaskRead(TaskBase):
    id: UUID
    predicted_duration: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: list[TagRead] = []

    # model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True

class TaskAddTags(BaseModel):
    tags: List[str]
