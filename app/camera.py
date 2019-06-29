import cv2 
import time 
import random
import string
key = cv2. waitKey(1)
webcam = cv2.VideoCapture(0)

def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
    
def startCam():
    while True:
        check, frame = webcam.read()
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