from sqlalchemy.orm import Session
from ..models.user_role import UserRole
from ..schemas import UserRoleCreate, UserRoleRead
from uuid import uuid4

def get_roles(db: Session):
    return db.query(UserRole).all()

def get_role(db: Session, role_id: int):
    return db.query(UserRole).filter(UserRole.id == role_id).first()

def create_role(db: Session, role: UserRoleCreate):
    db_role = UserRole(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

def update_role(db: Session, role_id: int, role: UserRoleCreate):
    db_role = get_role(db, role_id)
    if not db_role:
        return None
    for key, value in role.dict().items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role

def delete_role(db: Session, role_id: int):
    db_role = get_role(db, role_id)
    if not db_role:
        return None
    db.delete(db_role)
    db.commit()
    return db_role
