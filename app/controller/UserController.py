from app.model.user import Users
from app import response, app

def getList():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def getDetail(user_id):
    try:
        user = Users.query.filter_by(id=user_id).first()
        if not user:
            return response.badRequest([], "User not found")

        data = singleTransform(user)
        return response.ok(data, "")
    except Exception as e:
        print(e)


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