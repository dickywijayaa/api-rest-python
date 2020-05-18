from app.model.event import Events
from app.model.user import Users
from app import response, db
from app.controller import UserController
from app.constants.message import Message
from flask import request

def getList():
    try:
        events = Events.query.all()
        data = transform(events)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.internalServerError()


def getDetail(event_id):
    try:
        event = Events.query.filter_by(id=event_id).first()
        if not event:
            return response.badRequest([], Message.CONST_EVENT_NOT_FOUND)
        
        data = singleTransform(event)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        return response.internalServerError()


def transform(events):
    data = []
    for event in events:
        data.append(singleTransform(event))

    return data


def singleTransform(event):
    data = {
        'id': event.id,
        'event': event.event,
        'description': event.description,
        'created_at': event.created_at,
        'updated_at': event.updated_at,
        'user': UserController.singleTransform(event.users)
    }
    return data

def insert():
    try:
        input_name = request.json['name']
        input_description = request.json['description']
        input_user_id = request.json['user_id']
    except Exception as e:
        return response.badRequest("", Message.CONST_REQUIRED_INSERT_EVENT_VALIDATION)

    try:
        # Check user is exists
        user = Users.query.filter_by(id=input_user_id).first()
        if not user:
            return response.badRequest("", Message.CONST_USER_NOT_FOUND)

        event = Events(event=input_name, description=input_description, user_id=input_user_id)
        db.session.add(event)
        db.session.commit()
    
        data = singleTransform(event)
        return response.ok(data, Message.CONST_SUCCESS_INSERT_EVENT_MESSAGE)
    except Exception as e:
        print(e)
        return response.internalServerError()

def update(event_id):
    try:
        input_description = request.json['description']
    except Exception as e:
        return response.badRequest("", Message.CONST_REQUIRED_UPDATE_EVENT_VALIDATION)

    try:
        event = Events.query.filter_by(id=event_id).first()
        if not event:
            return response.badRequest([], Message.CONST_EVENT_NOT_FOUND)
        
        event.description = input_description
        db.session.commit()

        data = singleTransform(event)
        return response.ok(data, Message.CONST_SUCCESS_UPDATE_EVENT_MESSAGE)
    except Exception as e:
        print(e)
        return response.internalServerError()

def delete(event_id):
    try:
        event = Events.query.filter_by(id=event_id).first()
        if not event:
            return response.badRequest([], Message.CONST_EVENT_NOT_FOUND)
        
        db.session.delete(event)
        db.session.commit()

        return response.ok("", Message.CONST_SUCCESS_DELETE_EVENT_MESSAGE)
    except Exception as e:
        print(e)
        return response.internalServerError()