from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from ..db import db
from ..repositories.task_repository import TaskRepository

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    def to_dict(self):
        dictionary = {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "is_complete": isinstance(self.completed_at, datetime)
        }

        return dictionary

    def from_dict(self, record_data: dict):
        repo = TaskRepository()

        return repo.create(record_data)
