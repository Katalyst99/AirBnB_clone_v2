#!/usr/bin/python3
"""A script that starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Displays a HTML page with the list of all State objects present,
    in DBStorage sorted by name (A->Z)
    """
    name_state = storage.all(State)
    return render_template('9-states.html', name_state=name_state)


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    """Displays a HTML page If a State object is found with id"""
    stateId = storage.all(State).values()
    for state in stateId:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def handle_teardown(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
