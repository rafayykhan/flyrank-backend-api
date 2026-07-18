from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Task API", version="1.0")

tasks = [
    {"id": 1, "title": "Watch the W2 lecture", "done": True},
    {"id": 2, "title": "Read MDN: How the web works", "done": False},
    {"id": 3, "title": "Build the CRUD API", "done": False},
]

def find_task(task_id):
    return next((t for t in tasks if t["id"] == task_id), None)

def not_found(task_id):
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.get("/")
def root():
    return {"name": "Task API", "version": "1.0", "endpoints": ["/tasks"]}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/tasks")
def list_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        return not_found(task_id)
    return task