from sqlalchemy.orm import Session
from ..models.task_status import TaskStatus
from ..schemas.task_status import TaskStatusCreate

def get_statuses(db: Session):
    return db.query(TaskStatus).all()

def get_status(db: Session, status_id: int):
    return db.query(TaskStatus).filter(TaskStatus.id == status_id).first()

def create_status(db: Session, status: TaskStatusCreate):
    db_status = TaskStatus(**status.dict())
    db.add(db_status)
    db.commit()
    db.refresh(db_status)
    return db_status
