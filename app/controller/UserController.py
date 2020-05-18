from app.model.user import Users
from app import response, app
from app import db
from flask import request
from app.constants.message import Message

def getList():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.internalServerError()


def getDetail(user_id):
    try:
        user = Users.query.filter_by(id=user_id).first()
        if not user:
            return response.badRequest([], Message.CONST_USER_NOT_FOUND)

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.internalServerError()


def transform(users):
    array = []
    for user in users:
        array.append(singleTransform(user))

    return array


def singleTransform(user):
    data = {
        'id': user.id,
        'name': user.name,
        'email': user.email
    }
    return data

def insert():
    try:
        # To-DO: Validate Input
        input_name = request.json['name']
        input_email = request.json['email']
        input_password = request.json['password']
    except Exception as e:
        print(e)
        return response.badRequest("", Message.CONST_REQUIRED_INSERT_USER_VALIDATION)

    try:
        user = Users(name=input_name, email=input_email)
        user.setPassword(input_password)
        db.session.add(user)
        db.session.commit()

        data = singleTransform(user)
        return response.ok(data, Message.CONST_SUCCESS_INSERT_USER_MESSAGE)
    except Exception as e:
        print(e)
        return response.internalServerError()

def update(user_id):
    try:
        # To-DO: Validate Input
        input_email = request.json['email']
    except Exception as e:
        print(e)
        return response.badRequest("", Message.CONST_REQUIRED_UPDATE_USER_VALIDATION)

    try:
        user = Users.query.filter_by(id=user_id).first()
        if not user:
            return response.badRequest([], Message.CONST_USER_NOT_FOUND)

        user.email = input_email
        db.session.commit()

        data = singleTransform(user)
        return response.ok(data, Message.CONST_SUCCESS_UPDATE_USER_MESSAGE)
    except Exception as e:
        print(e)
        return response.internalServerError()