from pydantic import BaseModel, ConfigDict
from uuid import UUID

class TagBase(BaseModel):
    name: str

class TagRead(TagBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

class TagCreate(TagBase):
    pass

class TagResponse(TagBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True)

class TaskTagBase(BaseModel):
    task_id: UUID
    tag: str

class TaskTagCreate(TaskTagBase):
    pass

class TaskTagRead(TaskTagBase):
    id: UUID

    class Config:
        orm_mode = True
