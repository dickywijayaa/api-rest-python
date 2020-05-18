from app.model.event import Events
from app import response, db
from app.controller import UserController

def getList():
    events = Events.query.all()
    data = transform(events)
    return response.ok(data, "success retrieve data")

def transform(events):
    data = []
    for event in events:
        data.append({
            'id': event.id,
            'event': event.event,
            'description': event.description,
            'created_at': event.created_at,
            'updated_at': event.updated_at,
            'user': UserController.singleTransform(event.users)
        })

    return data