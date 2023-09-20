from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Team
from .controllers import index, show

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome to the football teams API!"
  }), 200

@app.route("/teams", methods=["GET", "POST"])
def handle_teams():
  if request.method == "GET":
    return index()

@app.route("/teams/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_team(id):
  if request.method == "GET":
    return show(id)