from fastapi import FastAPI

app = FastAPI(title="API", version= 1.0)

@app.get("/")

def root():
    return {"message": "Api is alive" }