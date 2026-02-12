from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class TaskStatusBase(BaseModel):
    status_name: str
    description: Optional[str] = None
    color: Optional[str] = "#FFFFFF"

class TaskStatusCreate(TaskStatusBase):
    pass

class TaskStatusRead(TaskStatusBase):
    id: UUID

    class Config:
        orm_mode = True
