from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import task_priority as crud
from ..schemas.task_priority import TaskPriorityCreate, TaskPriorityRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/task_priorities", tags=["Task Priorities"])

@router.get("/", response_model=list[TaskPriorityRead])
def list_priorities(db: Session = Depends(get_db)):
    return crud.get_priorities(db)

@router.get("/{priority_id}", response_model=TaskPriorityRead)
def get_priority(priority_id: UUID, db: Session = Depends(get_db)):
    return crud.get_priority(db, priority_id)

@router.post("/", response_model=TaskPriorityRead)
def create_priority(priority: TaskPriorityCreate, db: Session = Depends(get_db)):
    return crud.create_priority(db, priority)
