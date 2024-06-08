# main.py - Worker Node Application Entry Point

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Worker Node is up and running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
