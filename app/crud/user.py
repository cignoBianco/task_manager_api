from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas import UserCreate, UserRead, UserUpdate
from ..crud.user_role import get_role

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id, user: UserCreate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user_patch(db: Session, user_id, user_patch: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        update_data = user_patch.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)
        db.commit()
        db.refresh(user)
    return user

def delete_user(db: Session, user_id):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
