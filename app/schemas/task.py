from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID
from datetime import date, datetime

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
    tags: Optional[List[str]] = []

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: UUID
    predicted_duration: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
