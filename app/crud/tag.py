from sqlalchemy.orm import Session
from ..models.tag import Tag
from ..schemas import TaskTagCreate, TaskTagRead

def get_tags(db: Session):
    return db.query(Tag).all()

def get_tag(db: Session, tag_id):
    return db.query(Tag).filter(Tag.id == tag_id).first()

def create_tag(db: Session, tag: TaskTagCreate):
    db_tag = Tag(**tag.dict())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def update_tag(db: Session, tag_id, tag: TaskTagCreate):
    db_tag = get_tag(db, tag_id)
    if not db_tag:
        return None
    for key, value in tag.dict(exclude_unset=True).items():
        setattr(db_tag, key, value)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def delete_tag(db: Session, tag_id):
    db_tag = get_tag(db, tag_id)
    if not db_tag:
        return None
    db.delete(db_tag)
    db.commit()
    return db_tag
