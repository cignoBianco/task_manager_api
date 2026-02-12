from sqlalchemy.orm import Session
from ..models.project_status import ProjectStatus
from ..schemas.project_status import ProjectStatusCreate

def get_statuses(db: Session):
    return db.query(ProjectStatus).all()

def get_status(db: Session, status_id: int):
    return db.query(ProjectStatus).filter(ProjectStatus.id == status_id).first()

def create_status(db: Session, status: ProjectStatusCreate):
    db_status = ProjectStatus(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status
