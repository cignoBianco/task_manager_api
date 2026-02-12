from pydantic import BaseModel
from uuid import UUID

class TaskDependencyBase(BaseModel):
    task_id: UUID
    depends_on_task_id: UUID

class TaskDependencyCreate(TaskDependencyBase):
    pass

class TaskDependencyRead(TaskDependencyBase):
    id: UUID

    class Config:
        orm_mode = True
