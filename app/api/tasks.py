from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import task as crud_task
from ..schemas.task import TaskCreate, TaskRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=list[TaskRead])
def list_tasks(db: Session = Depends(get_db)):
    return crud_task.get_tasks(db)

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
