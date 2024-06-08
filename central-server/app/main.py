# main.py
from fastapi import FastAPI
from . import routes, models, auth, logging

app = FastAPI()

# Initialize logging
logging.configure_logging()

# Include routers
app.include_router(routes.router)
app.include_router(auth.router)

@app.on_event("startup")
async def startup_event():
    print("Starting up the central server...")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down the central server...")
