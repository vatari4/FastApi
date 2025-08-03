from abc import ABC, abstractmethod
from typing import List, Optional
from core.domain.entities import Task


class TaskRepository(ABC):
    @abstractmethod
    async def add_task(self, name: str, description: Optional[str] = None) -> int:
        pass

    @abstractmethod
    async def get_all_tasks(self) -> List[Task]:
        pass