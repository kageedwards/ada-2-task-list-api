from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    def to_dict(self):
        dictionary = {
            "id": self.id or None,
            "title": self.title or None,
            "description": self.description or None,
            "is_complete": isinstance(self.completed_at, datetime)
        }

        return dictionary

    def from_dict(self, record_data: dict):
        """
        I want to use the repository pattern, but from_dict() must be implemented like so
        """
        from ..repositories.task_repository import TaskRepository
        repo = TaskRepository()

        return repo.create(record_data)
