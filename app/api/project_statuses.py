from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..crud import project_status as crud
from ..schemas.project_status import ProjectStatusCreate, ProjectStatusRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/project_statuses", tags=["Project Statuses"])

@router.get("/", response_model=list[ProjectStatusRead])
def list_statuses(db: Session = Depends(get_db)):
    return crud.get_statuses(db)

@router.get("/{status_id}", response_model=ProjectStatusRead)
def get_status(status_id: UUID, db: Session = Depends(get_db)):
    return crud.get_status(db, status_id)

@router.post("/", response_model=ProjectStatusRead)
def create_status(status: ProjectStatusCreate, db: Session = Depends(get_db)):
    return crud.create_status(db, status)
