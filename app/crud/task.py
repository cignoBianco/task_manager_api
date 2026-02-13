from sqlalchemy import func
from sqlalchemy.orm import Session
from ..models.task import Task
from ..models.tag import Tag
from ..schemas import TaskCreate, TaskRead
from uuid import UUID

def get_tasks(
    db: Session,
    tag_ids: list[UUID] | None = None,
    skip: int = 0,
    limit: int = 20,
):
    query = db.query(Task)

    if tag_ids:
        query = (
            query
            .join(Task.tags)
            .filter(Tag.id.in_(tag_ids))
            .group_by(Task.id)
            .having(func.count(Tag.id) == len(tag_ids))
        )

    return query.offset(skip).limit(limit).all()

def get_task(db: Session, task_id):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task_data: TaskCreate):
    task = Task(**task_data.model_dump(exclude={"tags"}))

    tags = []
    for tag_name in task_data.tags:
        tag = db.query(Tag).filter(Tag.name == tag_name).first()
        if not tag:
            tag = Tag(name=tag_name)
            db.add(tag)
            db.flush()
        tags.append(tag)

    task.tags = tags

    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task(db: Session, task_id, task: TaskCreate):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    for key, value in task.dict(exclude_unset=True).items():
        setattr(db_task, key, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id):
    db_task = get_task(db, task_id)
    if not db_task:
        return None
    db.delete(db_task)
    db.commit()
    return db_task
