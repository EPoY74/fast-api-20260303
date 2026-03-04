from __future__ import annotations
from dataclasses import field

from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI()

fake_db: list[dict[str, Task]] = []


class TaskBase(BaseModel):
    """Класс для работы с todo записью"""

    # Запрещаю создание лишних полей
    # При неправильном поле выдастся ошибка, а
    # не упадет приложение
    model_config = ConfigDict(extra="forbid")

    # Заголовок задачи
    title: str | None = Field(min_length=1, max_length=200)

    # Описание задачи
    description: str | None = Field(min_length=1, max_length=2000)

    # Факт выполнения задачи
    is_completed: bool = False


class TaskDB(TaskBase):
    id: int


class TaskOut(TaskBase):
    id: int


# READ Чтение всех заданий
@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return fake_db


#  CREATE: создаю новую задачу
@app.post("/tasks")
def creat_task(task: Task):
    task_for_add = task.model_dump()
    task_for_add["id"] = len(fake_db) + 1
    fake_db.append(task_for_add)

    return {"message": "задача успешно создана", "task": task}


@app.get("/")
def read_root():
    return {"message": "Прграмма для хранения задач."}


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    mached = [task for task in fake_db if task.get("id") == task_id]
    return mached


# {"task:": fake_db[task_id], "name": f"Задача номер {task_id}"}
