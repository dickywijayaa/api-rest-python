from app import app
from app.controller import UserController
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

@app.route("/users/<id>", methods=['GET', 'PUT'])
def user_detail(id):
   if request.method == 'GET':
      return UserController.getDetail(id)
   else:
      return UserController.update(id)