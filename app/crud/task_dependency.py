from sqlalchemy.orm import Session
from ..models.task_dependency import TaskDependency
from ..schemas import TaskDependencyCreate, TaskDependencyRead

def get_dependencies(db: Session):
    return db.query(TaskDependency).all()

def get_dependency(db: Session, dep_id):
    return db.query(TaskDependency).filter(TaskDependency.id == dep_id).first()

def create_dependency(db: Session, dep: TaskDependencyCreate):
    db_dep = TaskDependency(**dep.dict())
    db.add(db_dep)
    db.commit()
    db.refresh(db_dep)
    return db_dep

def update_dependency(db: Session, dep_id, dep: TaskDependencyCreate):
    db_dep = get_dependency(db, dep_id)
    if not db_dep:
        return None
    for key, value in dep.dict(exclude_unset=True).items():
        setattr(db_dep, key, value)
    db.commit()
    db.refresh(db_dep)
    return db_dep

def delete_dependency(db: Session, dep_id):
    db_dep = get_dependency(db, dep_id)
    if not db_dep:
        return None
    db.delete(db_dep)
    db.commit()
    return db_dep
