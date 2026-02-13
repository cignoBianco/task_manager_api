from sqlalchemy.orm import Session
from ..models.tag import Tag
from uuid import UUID
from ..schemas import TaskTagCreate, TaskTagRead

def create_tag(db: Session, tag_create):
    tag = Tag(**tag_create.model_dump())
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

def get_tag_by_id(db: Session, tag_id: UUID):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def get_tag_by_name(db: Session, name: str):
    return db.query(Tag).filter(Tag.name == name).first()

def get_tags(db: Session, skip: int = 0, limit: int = 20):
    return db.query(Tag).offset(skip).limit(limit).all()

def delete_tag(db: Session, tag_id: UUID):
    tag = get_tag_by_id(db, tag_id)
    if tag:
        db.delete(tag)
        db.commit()
    return tag