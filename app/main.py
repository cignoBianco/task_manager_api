from fastapi import FastAPI
from .api import (
    users,
    projects,
    tasks,
    task_dependencies,
    tags,
    ml,
    task_priority,
    task_statuses,
    project_statuses,
    user_roles,
)
from .core.config.database import Base, engine

import os
print(os.getenv("DATABASE_URL"))

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(users.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(task_dependencies.router)
app.include_router(tags.router)
app.include_router(ml.router)
app.include_router(task_priority.router)
app.include_router(task_statuses.router)
app.include_router(project_statuses.router)
app.include_router(user_roles.router)
