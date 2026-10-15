from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Select
from ..models.base import Base as BaseModel

class BaseRepository:
    __MODEL: type[BaseModel]
    __db: SQLAlchemy

    def __init__(self, database: SQLAlchemy, model_class: type[BaseModel]):
        """ 
        Using a repository pattern for the validation layer

        We can create repository classes for each model that needs this CRUD validation layer
        by inheriting this class and overriding the base model it uses.

        The typehinting isn't necessary but is helpful for code completion.
        """
        self.__MODEL = model_class
        self.__db = database

    def query(self) -> Select:
        return self.__db.select(self.__MODEL)