from fastapi import APIRouter, Depends
from core.use_cases.task_use_cases import TaskUseCases
from infrastructure.database.repositories import DatabaseTaskRepository
from schemas.schemas import TaskCreate, Task as TaskSchema
from typing import Dict, List

router = APIRouter(prefix="/tasks", tags=["TASK"])

def get_task_use_cases() -> TaskUseCases:
    return TaskUseCases(DatabaseTaskRepository())

@router.post("", response_model=Dict[str, int | bool])
async def create_task(
    task_data: TaskCreate,
    use_cases: TaskUseCases = Depends(get_task_use_cases)
) -> Dict[str, int | bool]:
    task_id = await use_cases.create_task(task_data.name, task_data.description)
    return {"ok": True, "task_id": task_id}

@router.get("", response_model=List[TaskSchema])
async def list_tasks(
    use_cases: TaskUseCases = Depends(get_task_use_cases)
) -> List[TaskSchema]:
    tasks = await use_cases.list_tasks()
    return tasks