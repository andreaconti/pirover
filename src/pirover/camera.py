"""
Camera abstractions and utils for video streaming
"""

try:

    import time
    from PIL import Image
    import io

    from picamera.array import PiRGBArray
    from picamera import PiCamera

    def video_stream():

        # init camera
        camera = PiCamera()
        camera.resolution = (640, 480)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(640, 480))
        time.sleep(0.5)

        # video stream
        for frame in camera.capture_continuous(rawCapture, format="rgb", use_video_port=True):
            image = Image.fromarray(frame.array)
            buf = io.BytesIO()
            image.save(buf, format='JPEG')
            yield buf.getvalue()
            rawCapture.truncate(0)

except ModuleNotFoundError:

    import numpy as np
    from PIL import Image
    import time

    # if picamera is not available load an empty stream
    def video_stream():
        image = Image.fromarray(np.zeros(shape=(480, 640, 3), dtype=np.uint8))
        buf = io.BytesIO()
        image.save(buf, format='JPEG')
        byte_im = buf.getvalue()
        while True:
            yield byte_im
            time.sleep(5)
