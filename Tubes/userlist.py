# Data to serve with our API


USERLIST = {
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

# Create a handler for our read (GET) user
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of user

    :return:        sorted list of user
    """
    # Create the list of people from our data
    return [USERLIST[key] for key in sorted(USERLIST.keys())]
