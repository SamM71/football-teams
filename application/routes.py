from flask import jsonify, request
from werkzeug import exceptions
from application import app, db
from application.models import Team

@app.route("/")
def hello_world():
  return jsonify({
    "message": "Welcome to the football teams API!"
  }), 200