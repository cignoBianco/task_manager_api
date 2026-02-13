from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..models.user import User
from ..crud import user as crud_user
from ..schemas import UserCreate, UserRead, UserUpdate
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserRead])
def list_users(email: str | None = None,
    skip: int = 0,
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db)):
    query = db.query(User)

    if email:
        query = query.filter(User.email.ilike(f"%{email}%"))

    return query.offset(skip).limit(limit).all()

@router.get("/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud_user.get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=UserRead)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return crud_user.create_user(db, user)

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: UUID, user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud_user.update_user(db, user_id, user)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.patch("/{user_id}", response_model=UserRead)
def patch_user(user_id: UUID, user_patch: UserUpdate, db: Session = Depends(get_db)):
    user = crud_user.update_user_patch(db, user_id, user_patch)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=UserRead)
def delete_user(user_id: UUID, db: Session = Depends(get_db)):
    db_user = crud_user.delete_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
