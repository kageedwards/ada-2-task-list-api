from ..models.task import Task
from .base_repository import BaseRepository
from ..db import db
from datetime import datetime

class TaskRepository(BaseRepository):
    def __init__(self):
        super().__init__(db, Task)

    def validate(record_data: dict):
        try:
            title = record_data["title"]
            description = record_data.get("description", "")
            completed_at = record_data.get("completed_at", None)
        except KeyError:
            return False

        return {
            "title": title,
            "description": description,
            "completed_at": completed_at,
        }
        

    def create(self, record_data: dict):
        validated_data = self.validate(record_data)
        
        if not validated_data:
            return None

        new_task = self.__MODEL(
            title=validated_data["title"], 
            description=validated_data["description"], 
            completed_at=validated_data["completed_at"]
        )

        self.session().add(new_task)
        self.session().commit()

        return new_task