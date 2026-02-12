from pydantic import BaseModel
from uuid import UUID

class TaskTagBase(BaseModel):
    task_id: UUID
    tag: str

class TaskTagCreate(TaskTagBase):
    pass

class TaskTagRead(TaskTagBase):
    id: UUID

    class Config:
        orm_mode = True
