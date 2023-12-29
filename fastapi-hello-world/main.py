from fastapi import FastAPI, Request
from starlette.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/add/")
async def add_values(v1: int = 0, v2: int = 0):
    return v1 + v2