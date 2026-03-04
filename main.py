from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Привет!"}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    return {"task_id": task_id, "name": f"Задача номер {task_id}" }


@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return{
        "message": "Возвращаю список задач",
        "skip": skip,
        "limit": limit
    }
