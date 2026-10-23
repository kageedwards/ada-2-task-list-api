from datetime import datetime
from flask import Blueprint, request, Response, make_response, abort
from app.models.goal import Goal
from ..db import db
from .route_utilities import (
    validate_model, 
    create_model, 
    update_model, 
    get_models_with_filters, 
    quiet_success_response, 
    send_slack_notification
)

goals_bp = Blueprint("goals_bp", __name__, url_prefix="/goals")

@goals_bp.get("")
def get_all_goals():
    goals_response = get_models_with_filters(Goal, request.args)
    return goals_response

@goals_bp.get("/<goal_id>")
def get_one_goal(goal_id):
    goal = validate_model(Goal, goal_id)
    return goal.to_dict(), 200

@goals_bp.post("")
def create_goal():
    request_body = request.get_json()

    return create_model(Goal, request_body)

@goals_bp.put("/<goal_id>")
def update_goal(goal_id):
    this_goal = validate_model(Goal, goal_id)
    request_body = request.get_json()
    return update_model(this_goal, request_body)

@goals_bp.delete("/<goal_id>")
def delete_task(goal_id):
    goal = validate_model(Goal, goal_id)

    db.session.delete(goal)
    db.session.commit()

    return quiet_success_response()