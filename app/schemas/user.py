from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from uuid import UUID

class UserBase(BaseModel):
    name: str
    email: EmailStr
    role_id: Optional[UUID] = None

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: UUID

    class Config:
        orm_mode = True

class UserUpdate(UserBase):
    name: Optional[str] = None
    email: Optional[str] = None
    role_id: Optional[UUID] = None

    model_config = ConfigDict(from_attributes=True)
