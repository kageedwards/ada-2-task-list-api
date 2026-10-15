from ..models.task import Task
from .base_repository import BaseRepository
from ..db import db

class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(db, Task)