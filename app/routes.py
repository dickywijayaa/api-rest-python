from app import app
from app.controller import UserController, EventController
from flask import request

@app.route('/')
@app.route('/index')
def index():
   return "Hello, World!"


# user route
@app.route("/users", methods=['POST', 'GET'])
def users():
   if request.method == 'GET':
      return UserController.getList()
   else:
      return UserController.insert()

@app.route("/users/<id>", methods=['GET', 'PUT', 'DELETE'])
def user_detail(id):
   if request.method == 'GET':
      return UserController.getDetail(id)
   elif request.method == 'PUT':
      return UserController.update(id)
   else:
      return UserController.delete(id)


# event route
@app.route("/events", methods=['POST', 'GET'])
def events():
   if request.method == 'GET':
      return EventController.getList()
   else:
      return EventController.insert()

@app.route("/events/<id>", methods=['GET', 'PUT', 'DELETE'])
def event_detail(id):
   if request.method == 'GET':
      return EventController.getDetail(id)
   elif request.method == 'PUT':
      return EventController.update(id)
   else:
      return EventController.delete(id)