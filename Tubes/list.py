# 3rd party modules
from flask import make_response, abort

# Data to serve with our API


USER = {
    "leo": {
        "nama": "Leo Draconus",
        "bidang": "musik",
        "prestasi": "juara 2 lomba gitar akustik"
    },
    "catto": {
        "nama": "Catto Kawaii",
        "bidang": "cosplayer",
        "prestasi": "juara 3 lomba cosplay"
    }
}

# Create a handler for our read (GET) user
def read_all():
    """
    This function responds to a request for /api/user
    with the complete lists of user

    :return:        sorted list of user
    """
    # Create the list of people from our data
    return [USER[key] for key in sorted(USER.keys())]

def read_one(username):

    # Does the person exist in people?
    if username in USER:
        mahasiswa = USER.get(username)

    # otherwise, nope, not found
    else:
        abort(
            404, "Person with username {username} not found".format(username=username),
        )

    return mahasiswa
