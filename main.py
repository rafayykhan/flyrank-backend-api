from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Request, Response

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

@app.post("/tasks", status_code=201)
async def create_task(request: Request):
    try:
        body = await request.json()
    except Exception:
        body = {}

    title = str(body.get("title") or "").strip()
    if not title:
        return JSONResponse(status_code=400, content={"error": "title is required"})

    next_id = max((t["id"] for t in tasks), default=0) + 1
    task = {"id": next_id, "title": title, "done": False}
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, request: Request):
    task = find_task(task_id)
    if task is None:
        return not_found(task_id)

    try:
        body = await request.json()
    except Exception:
        body = {}

    if "title" not in body and "done" not in body:
        return JSONResponse(status_code=400, content={"error": "title or done is required"})

    if "title" in body:
        title = str(body.get("title") or "").strip()
        if not title:
            return JSONResponse(status_code=400, content={"error": "title cannot be empty"})
        task["title"] = title

    if "done" in body:
        if not isinstance(body["done"], bool):
            return JSONResponse(status_code=400, content={"error": "done must be true or false"})
        task["done"] = body["done"]

    return task

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    task = find_task(task_id)
    if task is None:
        return not_found(task_id)
    tasks.remove(task)
    return Response(status_code=204)