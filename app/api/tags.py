from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import tag as crud_tag
from ..schemas.tag import TaskTagCreate, TaskTagRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/tags", tags=["Task Tags"])

@router.get("/", response_model=list[TaskTagRead])
def list_tags(db: Session = Depends(get_db)):
    return crud_tag.get_tags(db)

@router.post("/", response_model=TaskTagRead)
def create_tag(tag: TaskTagCreate, db: Session = Depends(get_db)):
    return crud_tag.create_tag(db, tag)

@router.delete("/{tag_id}", response_model=TaskTagRead)
def delete_tag(tag_id: UUID, db: Session = Depends(get_db)):
    db_tag = crud_tag.delete_tag(db, tag_id)
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return db_tag
