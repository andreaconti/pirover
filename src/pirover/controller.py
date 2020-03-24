#!/usr/bin/env python3

"""
Vehicle controller module, here can be found all functionalities of the
vehicle, from movements to sensors
"""

import gpiozero
from threading import Timer
import time


class Controller:

    def __init__(self, left, right):
        self._left = gpiozero.Motor(*left)
        self._right = gpiozero.Motor(*right)
        self._stop = Timer(0.1, lambda: self.stop())
        self._stop.start()

    def _action_setup(self, action, wait, duration):
        self._stop.cancel()
        action()
        if not wait:
            self._stop = Timer(duration, lambda: self.stop())
            self._stop.start()
        else:
            time.sleep(duration)
            self.stop()

    def forward(self, wait=False, speed=1, duration=0.3):
        def forward_():
            self._left.forward(speed)
            self._right.forward(speed)
        self._action_setup(forward_, wait, duration)

    def backward(self, speed=1, wait=False, duration=0.3):
        def backward_():
            self._left.backward(speed)
            self._right.backward(speed)
        self._action_setup(backward_, wait, duration)

    def left(self, wait=False, duration=0.3):
        def left_():
            self._left.backward()
            self._right.forward()
        self._action_setup(left_, wait, duration)

    def right(self, wait=False, duration=0.3):
        def left_():
            self._left.forward()
            self._right.backward()
        self._action_setup(left_, wait, duration)

    def stop(self):
        self._left.stop()
        self._right.stop()
