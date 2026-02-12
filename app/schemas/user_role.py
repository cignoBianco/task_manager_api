from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class UserRoleBase(BaseModel):
    role_name: str
    description: Optional[str] = None

class UserRoleCreate(UserRoleBase):
    pass

class UserRoleRead(UserRoleBase):
    id: UUID

    class Config:
        orm_mode = True
