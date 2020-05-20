from flask import request, jsonify, make_response
from flask import current_app as app
from datetime import datetime as dt

# DEFINE YOUR ROUTES

"""
EXAMPLE

@app.route('/')
def index():
    my_dict = {'msg': 'welcome to the main page'}
    headers = {'Content-Type': 'application/json'}
    return make_response(jsonify(my_dict), 200, headers)
"""
