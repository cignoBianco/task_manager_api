from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TaskPriorityBase(BaseModel):
    priority_name: str
    weight: Optional[int] = 0
    color: Optional[str] = "#FFFFFF"

class TaskPriorityCreate(TaskPriorityBase):
    pass

class TaskPriorityRead(TaskPriorityBase):
    id: UUID

    class Config:
        orm_mode = True
