from app.model.event import Events
from app import response, db
from app.controller import UserController

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