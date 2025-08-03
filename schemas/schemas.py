from pydantic import BaseModel
from typing import Optional, Dict, Union

class TaskCreate(BaseModel):
    name: str
    description: Optional[str] = None

class Task(BaseModel):
    id: int
    name: str
    description: Optional[str] = None