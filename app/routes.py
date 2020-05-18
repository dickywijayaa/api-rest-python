from app import app
from app.controller import UserController

@app.route('/')
@app.route('/index')
def index():
   return "Hello, World!"

@app.route("/users")
def users():
   return UserController.index()