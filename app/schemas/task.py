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

class TaskStatusNested(BaseModel):
    id: UUID
    status_name: str

    class Config:
        from_attributes = True

class TaskRead(TaskBase):
    id: UUID
    predicted_duration: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    tags: list[TagRead] = []
    status_id: UUID
    status: TaskStatusNested

    # model_config = ConfigDict(from_attributes=True)

    class Config:
        orm_mode = True

class TaskAddTags(BaseModel):
    tags: List[str]


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None

    assignee_id: Optional[UUID] = None

    start_date: Optional[date] = None
    due_date: Optional[date] = None

    actual_end_date: Optional[date] = None

    status_id: Optional[UUID] = None
    priority_id: Optional[UUID] = None

    tags: Optional[list[str]] = None


class TaskFilter(BaseModel):
    project_id: Optional[UUID] = None

    status_id: Optional[UUID] = None

    status: Optional[str] = None

    assignee_id: Optional[UUID] = None
    tags: Optional[List[str]] = None

    limit: int = 20
    offset: int = 0
