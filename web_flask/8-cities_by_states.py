#!/usr/bin/python3
"""A script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
    Displays a HTML page with the list of  City objects linked to the State
    sorted by name (A->Z)
    """
    name_state = storage.all(State)
    return render_template('8-cities_by_states.html', name_state=name_state)


@app.teardown_appcontext
def handle_teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
