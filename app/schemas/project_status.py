from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ProjectStatusBase(BaseModel):
    status_name: str
    description: Optional[str] = None
    color: Optional[str] = "#FFFFFF"

class ProjectStatusCreate(ProjectStatusBase):
    pass

class ProjectStatusRead(ProjectStatusBase):
    id: UUID

    class Config:
        orm_mode = True
