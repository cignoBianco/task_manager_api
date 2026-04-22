# from app.crud.ml import predict_priority, predict_risk, recommend_assignee


class AIService:

    def analyze_task(self, task, developers):

        priority = ""#predict_priority(task)
        risk = ""#predict_risk(task)
        assignee = ""#recommend_assignee(task, developers)

        return {
            "priority": priority,
            "risk": risk,
            "assignee_id": assignee
        }