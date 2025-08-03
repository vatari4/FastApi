from typing import List, Optional  # Add this import
from sqlalchemy import select
from core.domain.repositories import TaskRepository
from core.domain.entities import Task
from infrastructure.database.models import TaskORM
from infrastructure.database.session import new_session


class DatabaseTaskRepository(TaskRepository):
    async def add_task(self, name: str, description: Optional[str] = None) -> int:
        async with new_session() as session:
            task = TaskORM(name=name, description=description)
            session.add(task)
            await session.flush()
            await session.commit()
            return task.id

    async def get_all_tasks(self) -> List[Task]:  # Now List is properly imported
        async with new_session() as session:
            query = select(TaskORM)
            result = await session.execute(query)
            tasks = result.scalars().all()
            return [Task(id=task.id, name=task.name, description=task.description) for task in tasks]