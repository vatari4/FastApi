from typing import List
from core.domain.entities import Task
from core.domain.repositories import TaskRepository


class TaskUseCases:
    def __init__(self, repository: TaskRepository):
        self.repository = repository

    async def create_task(self, name: str, description: str = None) -> int:
        return await self.repository.add_task(name, description)

    async def list_tasks(self) -> List[Task]:
        return await self.repository.get_all_tasks()