# 3rd party modules
from flask import make_response, abort

# Data to serve with our API


USER_ALL = {
    "leo": {
        "username": "leo",
        "email": "leo.draconus@gmail.com",
        "password": "qwerty",
        "publicdata": {
            "nama": "Leo Draconus",
            "bidang": "musik",
            "prestasi": "juara 2 lomba gitar akustik"
        }
    },
    "catto": {
        "username": "catto",
        "email": "catto.kawaii@gmail.com",
        "password": "abcde",
        "publicdata": {
            "nama": "Catto Kawaii",
            "bidang": "cosplayer",
            "prestasi": "juara 3 lomba cosplay"
        }
    }
}

def create(username):

    username = person.get("username", None)
    email = person.get("email", None)
    password = person.get("password", None)
    nama = person.get("nama", None)
    bidang = person.get("bidang", None)
    prestasi = person.get("prestasi", None)

    # Does the person exist already?
    if username not in USER_ALL and username is not None:
        USER_ALL[username] = {
            "username": username,
            "email": email,
            "password": password,
            "nama": nama,
            "bidang": bidang,
            "prestasi": prestasi,
        }
        return make_response(
            "{username} successfully created".format(username=username), 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406,
            "Person with last name {username} already exists".format(username=username),
        )
