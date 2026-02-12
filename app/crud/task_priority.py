from sqlalchemy.orm import Session
from ..models.task_priority import TaskPriority
from ..schemas.task_priority import TaskPriorityCreate

def get_priorities(db: Session):
    return db.query(TaskPriority).all()

def get_priority(db: Session, priority_id: int):
    return db.query(TaskPriority).filter(TaskPriority.id == priority_id).first()

def create_priority(db: Session, priority: TaskPriorityCreate):
    db_priority = TaskPriority(**priority.dict())
    db.add(db_priority)
    db.commit()
    db.refresh(db_priority)
    return db_priority
