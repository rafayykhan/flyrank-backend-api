# FLyRankAI-Backend-API

A small **in-memory CRUD API** for managing a to-do list — create, read, update,
and delete tasks — with interactive Swagger docs.

Built for the **FlyRank Internship · Backend Track · Week 2 · Assignment A1**.

> No database yet: tasks live in a Python list in memory. Restart the server and
> the data resets to the three seed tasks. That reset is the whole point — it's
> the reason databases (Week 3) exist.

**Stack:** Python 3.10+ · FastAPI · Uvicorn · Swagger UI (built in)

---

## Quick start

```bash
# 1. clone
git clone https://github.com/rafayykhan/tasks-api.git
cd tasks-api

# 2. create and activate a virtual environment
python -m venv venv
venv\Scripts\activate            # Windows
# source venv/bin/activate       # macOS / Linux

# 3. install dependencies
pip install -r requirements.txt

# 4. run
uvicorn main:app --reload
```

The one command that runs it: **`uvicorn main:app --reload`**

Then open **http://localhost:8000/docs** for interactive Swagger UI.

---

## Endpoints

| Method   | Path            | Description                | Status codes    |
|----------|-----------------|----------------------------|-----------------|
| `GET`    | `/`             | Describe the API           | `200`           |
| `GET`    | `/health`       | Liveness check             | `200`           |
| `GET`    | `/tasks`        | List all tasks             | `200`           |
| `GET`    | `/tasks/{id}`   | Get one task               | `200`, `404`    |
| `POST`   | `/tasks`        | Create a task              | `201`, `400`    |
| `PUT`    | `/tasks/{id}`   | Update a task              | `200`, `400`, `404` |
| `DELETE` | `/tasks/{id}`   | Delete a task              | `204`, `404`    |

Every error response carries a JSON message, e.g. `{ "error": "Task 99 not found" }`.

### The task object

```json
{
  "id": 1,
  "title": "Buy milk",
  "done": false
}
```

- `id` — number, assigned by the server (you never send it)
- `title` — text, required and non-empty on create/update
- `done` — true/false, defaults to `false` on create

---

## Example — `curl -i`

Reading a single task, showing the full response (status line, headers, body):

```
$ curl -i http://localhost:8000/tasks/1

HTTP/1.1 200 OK
date: Sat, 18 Jul 2026 09:00:00 GMT
server: uvicorn
content-length: 62
content-type: application/json

{"id":1,"title":"Watch the W2 lecture","done":true}
```

Requesting a task that doesn't exist returns a `404` with a JSON error:

```
$ curl -i http://localhost:8000/tasks/99

HTTP/1.1 404 Not Found
content-type: application/json

{"error":"Task 99 not found"}
```

Creating a task without a title is rejected — the server never trusts the client:

```
$ curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d "{}"

HTTP/1.1 400 Bad Request
content-type: application/json

{"error":"title is required"}
```

---

## Full CRUD cycle (copy-paste to try it)

```bash
# Read the list
curl -i http://localhost:8000/tasks

# Create a task            -> 201
curl -i -X POST http://localhost:8000/tasks \
  -H "Content-Type: application/json" -d "{\"title\":\"Buy milk\"}"

# Update it (mark done)    -> 200
curl -i -X PUT http://localhost:8000/tasks/2 \
  -H "Content-Type: application/json" -d "{\"done\":true}"

# Delete a task            -> 204 (empty body)
curl -i -X DELETE http://localhost:8000/tasks/1

# Confirm the changes
curl -i http://localhost:8000/tasks
```

---

## Swagger UI

Interactive docs are generated automatically by FastAPI at `/docs`. Every
endpoint is listed with a **Try it out** button that sends real requests — curl
with a friendly face.

![Swagger UI showing the full CRUD API](docs/swagger.png)

> Replace this with your own screenshot: run the server, open
> `http://localhost:8000/docs`, and save the image as `docs/swagger.png`.

---

## Project structure

```
tasks-api/
├── main.py            # the whole API — under 100 lines
├── requirements.txt   # fastapi, uvicorn
├── README.md          # this file
├── .gitignore
└── docs/
    └── swagger.png    # Swagger UI screenshot
```

---

## Notes on some design choices

A few things are done deliberately, because the exact status codes and body
shapes are part of the spec:

- **Errors use `JSONResponse`** so the body is exactly `{ "error": "..." }`.
  FastAPI's `HTTPException` would return `{ "detail": "..." }` — the wrong shape.
- **`POST`/`PUT` read the raw request body** instead of a Pydantic model, so a
  missing/empty title returns a clean `400` (a model would auto-return `422`).
- **`DELETE` returns a bare `204`** with a genuinely empty body.

---

## The mortality experiment

Create a few tasks, restart the server, then `GET /tasks`.

The tasks you created are gone — the list resets to the three seed tasks. Data
kept only in memory disappears the moment the process stops. That's exactly the
problem a database solves, which is where Week 3 picks up.

---

## AI vs me (Stage 7 — bonus)

_I wrote this API by hand first, then asked an AI to build the same thing from a
prompt I wrote from memory. The AI's code lives in `ai-version/` (untouched from
my hand-built submission)._

**My prompt:**

```
(paste the full prompt you wrote from memory here)
```

**Three concrete differences I found:**

1. _What the AI did better — and can I explain its version?_ …
2. _What it got wrong or ignored from my prompt (a missing 400? a wrong code? a
   database I never asked for?)_ …
3. _What my prompt forgot to specify — what did the AI silently decide for me?_ …

**One improved rematch:** _what I changed in my prompt, and what changed in the
output._ …

---

Built by **Rafay** · FlyRank Backend Track · Week 2. All tooling is free, no
credit card required.
