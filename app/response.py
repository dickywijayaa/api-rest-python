from app.constants.message import Message
from flask import jsonify, make_response


def ok(data, message):
    res = {
        'data': data,
        'message': message
    }

    return make_response(jsonify(res)), 200


def badRequest(data, message):
    res = {
        'data': data,
        'message': message
    }

    return make_response(jsonify(res)), 400

def internalServerError():
    res = {
        'message': Message.CONST_MESSAGE_INTERNAL_SERVER_ERROR
    }

    return make_response(jsonify(res)), 500

def httpNotFound():
    res = {
        'message': Message.CONST_HTTP_NOT_FOUND_MESSAGE
    }

    return make_response(jsonify(res)), 404