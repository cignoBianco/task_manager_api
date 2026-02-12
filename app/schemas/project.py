from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class ProjectBase(BaseModel):
    name: str
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    status_id: Optional[UUID] = None
    manager_id: Optional[UUID] = None

class ProjectCreate(ProjectBase):
    pass

class ProjectRead(ProjectBase):
    id: UUID

    class Config:
        orm_mode = True
