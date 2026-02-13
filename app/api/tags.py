from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.schemas.tag import TagCreate, TagResponse
from app.crud.tag import *
from ..schemas.tag import TaskTagCreate, TaskTagRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/tags", tags=["Task Tags"])

@router.post("/", response_model=TagResponse)
def create(tag: TagCreate, db: Session = Depends(get_db)):
    existing = get_tag_by_name(db, tag.name)
    if existing:
        raise HTTPException(status_code=400, detail="Tag already exists")
    return create_tag(db, tag)

@router.get("/", response_model=list[TagResponse])
def list_tags(
    skip: int = 0,
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    return get_tags(db, skip, limit)

@router.get("/{tag_id}", response_model=TagResponse)
def get(tag_id: UUID, db: Session = Depends(get_db)):
    tag = get_tag_by_id(db, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.delete("/{tag_id}")
def delete(tag_id: UUID, db: Session = Depends(get_db)):
    tag = delete_tag(db, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return {"detail": "Deleted"}
