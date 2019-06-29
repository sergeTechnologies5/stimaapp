import cv2
import sys
import pytesseract
def getOCR(value = 'app/static/img/camera/default.jpg'):
    # Read image path from command line
    imPath = value

    # Uncomment the line below to provide path to tesseract manually
    pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'
    
    # Define config parameters.
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')
    # Read image from disk
    im = cv2.imread(imPath, cv2.IMREAD_COLOR)
    
    # Run tesseract OCR on image
    text = pytesseract.image_to_string(im, config=config)
    # Print recognized text
    return text
if __name__ == '__main__':
    print(getOCR())