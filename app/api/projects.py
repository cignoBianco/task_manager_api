from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import project as crud_project
from ..schemas.project import ProjectCreate, ProjectRead
from ..core.config.database import get_db
from uuid import UUID

router = APIRouter(prefix="/projects", tags=["Projects"])

@router.get("/", response_model=list[ProjectRead])
def list_projects(db: Session = Depends(get_db)):
    return crud_project.get_projects(db)

@router.post("/", response_model=ProjectRead)
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return crud_project.create_project(db, project)

@router.put("/{project_id}", response_model=ProjectRead)
def update_project(project_id: UUID, project: ProjectCreate, db: Session = Depends(get_db)):
    db_project = crud_project.update_project(db, project_id, project)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

@router.delete("/{project_id}", response_model=ProjectRead)
def delete_project(project_id: UUID, db: Session = Depends(get_db)):
    db_project = crud_project.delete_project(db, project_id)
    if not db_project:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project
