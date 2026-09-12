from fastapi import FastAPI 
app=FastAPI()

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
