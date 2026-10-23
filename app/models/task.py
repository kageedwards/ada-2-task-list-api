from datetime import datetime
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Task(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    completed_at: Mapped[Optional[datetime]]

    # belongs to one Goal relationship
    goal_id: Mapped[Optional[int]] = mapped_column(ForeignKey("goal.id"))
    goal: Mapped[Optional["Goal"]] = relationship(back_populates="tasks") # noqa: F821

    @classmethod
    def sort_column(cls):
        return "title"

    def to_dict(self):
        dictionary = {
            "id": self.id or None,
            "title": self.title or None,
            "description": self.description or "",
            "is_complete": isinstance(self.completed_at, datetime)
        }

        return dictionary

    @classmethod
    def from_dict(cls, record_data: dict):
        completed_at = None

        if "completed_at" in record_data:
            completed_at = record_data["completed_at"]

            if not isinstance(completed_at, datetime):
                raise ValueError("The completed_at attribute is malformed")

        elif "is_complete" in record_data:
            if record_data["is_complete"] is False:
                completed_at = None

            elif request_body["is_complete"] is True:
                completed_at = datetime.now()

        return cls(
            title=record_data["title"],
            description=record_data["description"],
            completed_at=completed_at
        )