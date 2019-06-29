import cv2 
import time 
import random
import string
key = cv2. waitKey(1)


essing the Raspberry Pi Camera with OpenCV and PythonPython
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array

# display the image on screen and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
def startCam():
    while True:
        rawCapture = PiRGBArray(camera)
        # grab an image from the camera
        camera.capture(rawCapture, format="bgr")
        frame = rawCapture.array
        key = cv2.waitKey(1)
        image_url = randomString(5)+'.jpg'
        filepath = 'static/img/camera/'+image_url
        cv2.imwrite(filename=filepath, img=frame)
        img_new = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        cv2.waitKey(1650)
        time.sleep(10)
        print("Image saved!")
        if key == ord('q'):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            break

if __name__ == "__main__":
    startCam()