"""
Flask main server
"""

from flask import jsonify, request, Flask, render_template, Response

# APP

app = Flask(
    __name__,
    static_folder='static/dist',
    template_folder='static',
)

# DEPENDENCIES

actions = {}

video_gen = None


# GUI

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# REST API

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


def gen():
    while True:
        frame = next(video_gen)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(
            gen(),
            mimetype='multipart/x-mixed-replace; boundary=frame'
           )


@app.route('/api/action/move', methods=['POST'])
def api_action_move():
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
