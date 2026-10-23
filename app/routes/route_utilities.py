import math
from flask import abort, make_response
from sqlalchemy import desc
from ..db import db
from sqlalchemy import inspect


def validate_model(model, model_id):
    try:
        model_id = int(model_id)
    except (ValueError, TypeError):
        abort(make_response(
            {"message": f"{model.__name__.lower()} {model_id} invalid"},
            400
        ))

    instance = db.session.get(model, model_id)

    if instance is None:
        abort(make_response(
            {"message": f"{model.__name__.lower()} {model_id} not found"},
            404
        ))

    return instance

def create_model(cls, model_data):
    try:
        new_model = cls.from_dict(model_data)
    except KeyError as error:
        response = {"message": f"Invalid request: missing {error.args[0]}"}
        abort(make_response(response, 400))
    
    db.session.add(new_model)
    db.session.commit()

    return new_model.to_dict(), 201

def update_model(model, updated_data):
    attributes = [attr.key for attr in inspect(model.__class__).mapper.column_attrs]

    for attr in attributes:
        if attr in updated_data and attr != "id":
            setattr(model, attr, updated_data[attr])
    
    db.session.commit()

    return model.to_dict(), 200

def get_models_with_filters(cls, filters=None):
    query = db.select(cls)

    if filters and isinstance(filters, dict):
        for column, value in filters.items():
            if hasattr(cls, column):
                query = query.where(getattr(cls, column).ilike(f"%{value}%"))

    models = db.session.scalars(query)
    models_response = [model.to_dict() for model in models]

    return models_response