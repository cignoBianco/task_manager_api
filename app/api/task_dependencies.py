from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import task_dependency as crud_dep
from ..schemas.task_dependency import TaskDependencyCreate, TaskDependencyRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/task-dependencies", tags=["Task Dependencies"])

@router.get("/", response_model=list[TaskDependencyRead])
def list_dependencies(db: Session = Depends(get_db)):
    return crud_dep.get_dependencies(db)

@router.post("/", response_model=TaskDependencyRead)
def create_dependency(dep: TaskDependencyCreate, db: Session = Depends(get_db)):
    return crud_dep.create_dependency(db, dep)

@router.delete("/{dep_id}", response_model=TaskDependencyRead)
def delete_dependency(dep_id: UUID, db: Session = Depends(get_db)):
    db_dep = crud_dep.delete_dependency(db, dep_id)
    if not db_dep:
        raise HTTPException(status_code=404, detail="Dependency not found")
    return db_dep
