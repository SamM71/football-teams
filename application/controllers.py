from .models import Team
from werkzeug import exceptions
from flask import jsonify, request
from . import db

def index():
  try:
    teams = Team.query.all()
    data = [t.json for t in teams]
    return jsonify({"teams": data})
  except:
    raise exceptions.NotFound("Couldn't find any teams")
  
def show(id):
  try:
    team = Team.query.filter_by(id=id).first()
    return jsonify({"data": team.json}), 200
  except:
    raise exceptions.NotFound("Couldn't find team")

def create():
  try:
    name, nation, tier = request.json.values()
    new_team = Team(name, nation, tier)
    db.session.add(new_team)
    db.session.commit()
    return jsonify({"data": new_team.json}), 201
  except:
    raise exceptions.BadRequest(f"Sorry, we cannot process your request.")
  
def update(id):
  try:
    data = request.json
    team = Team.query.filter_by(id=id).first()

    for (attribute, value) in data.items():
      if hasattr(team, attribute):
        setattr(team, attribute, value)

    db.session.commit()
    return jsonify({"data": team.json}), 200
  except:
    raise exceptions.BadRequest(f"Sorry, we cannot process your request.")
  
def delete(id):
  try:
    team = Team.query.filter_by(id=id).first()
    db.session.delete(team)
    db.session.commit()
    return f"Team deleted", 200
  except:
    raise exceptions.BadRequest(f"Sorry, we cannot process your request.")