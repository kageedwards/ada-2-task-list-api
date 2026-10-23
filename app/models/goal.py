from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Goal(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]

    def to_dict(self):
        dictionary = {
            "id": self.id or None,
            "title": self.title or None
        }

        return dictionary

    @classmethod
    def from_dict(cls, record_data: dict):
        return cls(
            title=record_data["title"]
        )