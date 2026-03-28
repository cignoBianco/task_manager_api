from sqlalchemy.orm import Session
from app.crud import task as crud_task
from app.services.ai_service import AIService


class TaskService:

    def __init__(self):
        self.ai = AIService()

    def create_task(self, db: Session, data):

        task = crud_task.create_task(db, data)

        # AI analys
        developers = []  # потом из БД
        ai_result = self.ai.analyze_task(task, developers)

        # update task
        task.priority = ai_result["priority"]
        task.assignee_id = ai_result["assignee_id"]

        db.commit()
        db.refresh(task)

        return task