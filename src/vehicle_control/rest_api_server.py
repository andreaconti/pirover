"""
Flask main server
"""

from flask import jsonify, request
from flask import Blueprint
from vehicle_control.controller import Controller

# ACTIONS

actions = {}

# REST API

api = Blueprint('rest_api', __name__)


def _make_error(error):
    return jsonify({
        'done': False,
        'err': error
    })


def _ok():
    return jsonify({
        'done': True,
        'err': None
    })


@api.route('/vehicle/api/action/move', methods=['POST'])
def action_move():
    """
    Handles requests with a body of type json in the format:
    { "direction": <left|right|forward|backward>
    , "args": { <args for specific action> }
    }

    Sends responses in the format:
    { "done": True|False
    , "err" : null|string
    }
    """
    if not request.json:
        return _make_error(f'only json accepted'), 400

    try:
        action = request.json['direction']
        args = request.json['args']

        if action not in actions:
            return _make_error(f'action {action} not available', 400)
        else:
            actions[action](**args)
            return _ok(), 200

    except KeyError as e:
        return _make_error(f'invalid key {e}'), 400
