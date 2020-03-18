"""
Main program
"""

from vehicle_control import app
import vehicle_control.rest_api_server as rest_api_server
from vehicle_control.controller import Controller
import argparse


def main():

    # arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=3000, help='port of the web server')
    parser.add_argument('--motors', type=int, nargs=4, help='raspberry 4 left and right GPIO motors pins')
    args = vars(parser.parse_args())

    # setup controller server api
    if 'motors' in args:
        l1, l2, r1, r2 = args['motors']
        controller = Controller(left=(l1, l2), right=(r1, r2))
        actions = {
            'forward': controller.forward,
            'backward': controller.backward,
            'left': controller.left,
            'right': controller.right
        }
        rest_api_server.actions = actions
    else:
        print('error: must provide motors gpio pins by command line or in config file')
        exit(1)

    # start
    app.register_blueprint(rest_api_server.api)
    app.run(host='0.0.0.0', port=args['port'])


if __name__ == '__main__':
    main()
