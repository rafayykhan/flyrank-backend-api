# FlyRank AI-Backend-API

A small in-memory CRUD API for managing a to-do list. Built for the FlyRank
Backend Track, Week 2 (Assignment A1). No database — tasks live in memory and
reset when the server restarts.

Stack: Python + FastAPI. Interactive docs (Swagger UI) come built in.

## Run it

```bash
python -m venv venv
venv\Scripts\activate            # Windows
# source venv/bin/activate       # macOS / Linux
pip install -r requirements.txt
uvicorn main:app --reload
```

Then open **http://localhost:8000/docs** for Swagger UI.

## Endpoints

| Method | Path          | Description         | Status codes  |
|--------|---------------|---------------------|---------------|
| GET    | `/`           | Describe the API    | 200           |
| GET    | `/health`     | Liveness check      | 200           |
| GET    | `/tasks`      | List all tasks      | 200           |
| GET    | `/tasks/{id}` | Get one task        | 200, 404      |
| POST   | `/tasks`      | Create a task       | 201, 400      |
| PUT    | `/tasks/{id}` | Update a task       | 200, 400, 404 |
| DELETE | `/tasks/{id}` | Delete a task       | 204, 404      |

A task looks like: `{ "id": 1, "title": "Buy milk", "done": false }`

## Example (curl -i)

```
$ curl -i http://localhost:8000/tasks/1

(paste your real output here — status line, headers, and JSON body)
```

## Swagger UI

![Swagger UI](docs/swagger.png)

<!-- Take a screenshot of http://localhost:8000/docs, save it as docs/swagger.png -->

## AI vs me (Stage 7 — bonus)

<!--
Paste the full prompt you wrote from memory, then answer:
1. What did the AI do better — and can you explain its version?
2. What did it get wrong or ignore from your prompt?
3. What did your prompt forget to specify — what did the AI decide for you?
Then note one thing you changed in your improved prompt.
-->
