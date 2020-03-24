"""
Camera abstractions and utils for video streaming
"""

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
from typing import Generator


def video_stream() -> Generator:

    # init camera
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640, 480))
    time.sleep(0.5)

    # video stream
    for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
        image = frame.array
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')
        rawCapture.truncate(0)
