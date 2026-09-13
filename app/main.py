from fastapi import FastAPI 
from app.routers import read
from app.routers import create
from app.routers import update_delete

app=FastAPI()
app.include_router(read.router)
app.include_router(create.router)
app.include_router(update_delete.router)

@app.get("/")
def start_server():
    return {
        "message":"Hello Server"
        "name": "Task API", 
        "version": "1.0", 
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def get_health():
    return{
        "status":"ok"
    }
