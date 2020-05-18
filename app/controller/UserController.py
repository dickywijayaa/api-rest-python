from app.model.user import Users
from app import response, app

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)

def transform(users):
    array = []
    for user in users:
        array.append({
            'id': user.id,
            'name': user.name,
            'email': user.email
        })
    return array