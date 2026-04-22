from sqlalchemy.orm import Session
from app.crud import task as crud_task
from app.services.ai_service import AIService
from uuid import UUID
from app.models.task import Task


class TaskService:

    def __init__(self):
        self.ai = AIService()

    @staticmethod
    def create_task(self, db: Session, data):

        task = crud_task.create_task(db, data)

        # AI analys
        developers = []  # потом из БД
        ai_result = self.ai.analyze_task(task, developers)

        # update task
        task.priority = ai_result["priority"]
        task.assignee_id = ai_result["assignee_id"]

        # db.commit()
        # db.refresh(task)
        tags = TaskService.generate_tags_stub(data.title)
        crud.task.add_tags_to_task(db, task.id, tags)

        return task

    @staticmethod
    def generate_tags_stub(text: str):
        if "bug" in text.lower():
            return ["bug"]
        if "api" in text.lower():
            return ["backend"]
        return ["general"]

    @staticmethod
    def get_tasks(db: Session, filters):
        return crud_task.get_tasks_filtered(db, filters)