from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import user_role as crud
from ..schemas.user_role import UserRoleCreate, UserRoleRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/user_roles", tags=["User Roles"])

@router.get("/", response_model=list[UserRoleRead])
def list_roles(db: Session = Depends(get_db)):
    return crud.get_roles(db)

@router.get("/{role_id}", response_model=UserRoleRead)
def get_role(role_id: UUID, db: Session = Depends(get_db)):
    return crud.get_role(db, role_id)

@router.post("/", response_model=UserRoleRead)
def create_role(role: UserRoleCreate, db: Session = Depends(get_db)):
    return crud.create_role(db, role)
