#!/usr/bin/python3
"""A script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """
    Displays a HTML page with the list of all State objects present, 
    in DBStorage sorted by name (A->Z
    """
    name_state = storage.all(State)
    return render_template('')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
