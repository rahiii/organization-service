# src/main.py
from fastapi import FastAPI

app = FastAPI(
    title="Organization Profile Service",
    description="API for managing organization profiles.",
    version="1.0.0"
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Organization Profile Service!"}

