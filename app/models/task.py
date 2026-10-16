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

    def from_dict(record_data: dict):
        if record_data["is_complete"]:
            completed_at = record_data.get("completed_at", None)

            if completed_at is not None and not isinstance(completed_at, datetime):
                raise ValueError("The completed_at attribute is malformed")
        else:
            completed_at = None

        return Task(
            title=record_data["title"],
            description=record_data["description"],
            completed_at=completed_at
        )