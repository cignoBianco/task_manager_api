from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from ..crud import task as crud_task
from ..schemas.task import TaskCreate, TaskRead, TaskAddTags
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskRead])
def list_tasks(
    tag_ids: list[UUID] | None = Query(None),
    skip: int = 0,
    limit: int = Query(20, le=100),
    db: Session = Depends(get_db),
):
    return crud_task.get_tasks(db, tag_ids, skip, limit)

@router.post("/", response_model=TaskRead)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud_task.create_task(db, task)

@router.put("/{task_id}", response_model=TaskRead)
def update_task(task_id: UUID, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = crud_task.update_task(db, task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=TaskRead)
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    db_task = crud_task.delete_task(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.post("/{task_id}/tags", response_model=TaskRead)
def add_tags(
    task_id: UUID,
    payload: TaskAddTags,
    db: Session = Depends(get_db),
):
    task = crud_task.add_tags_to_task(db, task_id, payload.tags)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
