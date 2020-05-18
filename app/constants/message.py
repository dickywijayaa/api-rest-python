

class Message():
    # status response message
    CONST_HTTP_NOT_FOUND_MESSAGE = "route not found!"
    CONST_MESSAGE_INTERNAL_SERVER_ERROR = "something went wrong"

    # User
    CONST_USER_NOT_FOUND = "User not found"
    CONST_SUCCESS_INSERT_USER_MESSAGE = "Success insert user to db!"
    CONST_SUCCESS_UPDATE_USER_MESSAGE = "Success update user to db!"
    CONST_SUCCESS_DELETE_USER_MESSAGE = "Success delete user from db!"
    CONST_REQUIRED_INSERT_USER_VALIDATION = "name, email and password is required"
    CONST_REQUIRED_UPDATE_USER_VALIDATION = "email is required"

    # Event
    CONST_EVENT_NOT_FOUND = "Event not found"
    CONST_SUCCESS_INSERT_EVENT_MESSAGE = "Success insert event to db!"
    CONST_SUCCESS_UPDATE_EVENT_MESSAGE = "Success update event to db!"
    CONST_SUCCESS_DELETE_EVENT_MESSAGE = "Success delete event from db!"
    CONST_REQUIRED_INSERT_EVENT_VALIDATION = "name, description and user_id is required"
    CONST_REQUIRED_UPDATE_EVENT_VALIDATION = "description is required"