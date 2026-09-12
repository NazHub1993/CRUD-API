from fastapi import FastAPI 
from app.routers import read

app=FastAPI()
app.include_router(read.router)

@app.get("/")
def start_server():
    return {
        "name": "Task API", 
        "version": "1.0", 
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def get_health():
    return{
        "status":"ok"
    }
