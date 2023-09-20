from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Team
from .controllers import index, show, create, update, delete

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome to the football teams API!"
  }), 200

@app.route("/teams", methods=["GET", "POST"])
def handle_teams():
  if request.method == "GET":
    return index()
  if request.method == "POST":
    return create()

@app.route("/teams/<int:id>", methods=["GET", "PATCH", "DELETE"])
def handle_team(id):
  if request.method == "GET":
    return show(id)
  if request.method == "PATCH":
    return update(id)
  if request.method == "DELETE":
    return delete(id)