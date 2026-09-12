from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.routers.read import tasks


class Task(BaseModel):
    title: str


router = APIRouter(prefix="/create")


@router.post("/tasks")
def create_task(new_task: Task):
    if not new_task.title.strip():
        raise HTTPException(
            status_code=400,
            detail="No Title"
        )

    temp = {
        "id": len(tasks)+1,
        "title": new_task.title,
        "done": False
    }

    tasks.append(temp)

    raise HTTPException(
        status_code=201, detail=f"Task-{temp["id"]}:{temp["title"]} created")
