from fastapi import APIRouter, HTTPException
from app.routers.read import tasks
from typing import Optional
from pydantic import BaseModel


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


router = APIRouter(prefix="/tasks")


@router.put("/{id}")
def update_task(id: int, task_up: TaskUpdate):

    if task_up.title is None and task_up.done is None:
        raise HTTPException(
            status_code=400,
            detail="Request Body Empty"
        )

    for task in tasks:
        if task["id"] == id:
            if task_up.title is not None:
                if not task_up.title.strip():
                    raise HTTPException(status_code=400, detail="Title Empty")

                task["title"] = task_up.title

            if task_up.done is not None:
                task["done"] = task_up.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task:{id} not found"
    )


@router.delete("/{id}")
def delete_task(id: int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return {"message": f"Task : {id} removed"}

    raise HTTPException(
        status_code=404,
        detail="task not found"
    )
