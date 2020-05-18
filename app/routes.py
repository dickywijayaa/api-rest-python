from app import app
from app.controller import UserController

@app.route('/')
@app.route('/index')
def index():
   return "Hello, World!"

# user route
@app.route("/users")
def users():
   return UserController.getList()

@app.route("/users/<id>")
def user_detail(id):
   return UserController.getDetail(id)