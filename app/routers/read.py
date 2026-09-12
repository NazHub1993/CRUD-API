from fastapi import APIRouter, HTTPException

router=APIRouter(prefix="/tasks")

tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Build a CRUD API",
        "done": False
    },
    {
        "id": 3,
        "title": "Push project to GitHub",
        "done": False
    }
]

@router.get("")
def get_tasks():
    return tasks

@router.get("/{id}")
def get_task_by_id(id:int):
    for task in tasks:
        if task["id"]==id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"task-{id} not found"
    )
