import random
import string
import time
from picamera import PiCamera
from ocr import getOCR
camera = PiCamera()
camera.rotation = 180
camera.start_preview(alpha = 200)
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def startCam():
    while True:
        imageName = randomString(stringLength=5)+'.jpg'
        imagePath = 'static/img/camera/' + imageName
        camera.capture(imagePath)

        value = getOCR(imagePath)
        if value == None:
            value = getOCR()
        print("value  saved is = " + value)
        time.sleep(4)
    camera.stop_preview()

if __name__ == "__main__":
    startCam()