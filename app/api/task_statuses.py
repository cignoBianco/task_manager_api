from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import task_status as crud
from ..schemas.task_status import TaskStatusCreate, TaskStatusRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/task_statuses", tags=["Task Statuses"])

@router.get("/", response_model=list[TaskStatusRead])
def list_statuses(db: Session = Depends(get_db)):
    return crud.get_statuses(db)

@router.get("/{status_id}", response_model=TaskStatusRead)
def get_status(status_id: UUID, db: Session = Depends(get_db)):
    return crud.get_status(db, status_id)

@router.post("/", response_model=TaskStatusRead)
def create_status(status: TaskStatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db, status)
