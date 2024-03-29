import flask
import json
from flask import request, jsonify, current_app

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Create some test data for our catalog in the form of a list of dictionaries.
with open('USER_DATA.json', 'r') as myfile:
    data=myfile.read()

# parse file
users = json.loads(data)

@app.route('/')
def home():
    return current_app.send_static_file('index.html')


@app.route('/users/all', methods=['GET'])
def api_all():
    return jsonify(users)


@app.route('/users', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'name' in request.args:
        name = (request.args['name'])
    else:
        return "Error: No id field provided. Please specify an id."

    # Create an empty list for our results
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for user in users:
        if name.lower() in user['name'].lower():
            results.append(user)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)

app.run()