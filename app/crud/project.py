from sqlalchemy.orm import Session
from ..models.project import Project
from ..schemas import ProjectCreate, ProjectRead

def get_projects(db: Session):
    return db.query(Project).all()

def get_project(db: Session, project_id):
    return db.query(Project).filter(Project.id == project_id).first()

def create_project(db: Session, project: ProjectCreate):
    db_project = Project(**project.dict())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

def update_project(db: Session, project_id, project: ProjectCreate):
    db_project = get_project(db, project_id)
    if not db_project:
        return None
    for key, value in project.dict(exclude_unset=True).items():
        setattr(db_project, key, value)
    db.commit()
    db.refresh(db_project)
    return db_project

def delete_project(db: Session, project_id):
    db_project = get_project(db, project_id)
    if not db_project:
        return None
    db.delete(db_project)
    db.commit()
    return db_project
