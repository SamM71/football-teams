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

