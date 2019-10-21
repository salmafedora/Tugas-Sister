# 3rd party modules
from flask import make_response, abort

# Data to serve with our API


USER_PRIVATE = {
    "leo": {
        "username": "leo",
        "password": "qwerty"
    },
    "catto": {
        "username": "catto",
        "password": "abcde"
    }
}

def enter(username):

    username = person.get("username", None)
    password = person.get("password", None)

    # Does the person exist already?
    if username not in USER_PRIVATE and username is not None:
        USER_PRIVATE[username] = {
            "username": username,
            "password": password,
        }
        return make_response(
            "{username} successfully logged in".format(username=username), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with username {username} already logged in".format(username=username),
        )
