import cv2
import sys
import pytesseract
import sqlite3
from datetime import datetime
connection = sqlite3.connect("app.db")
def getOCR(value = 'static/img/camera/default.png'):
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
    cursor = connection.cursor()
    date = str(datetime.now())
    try:
        cost =  0.03
    except Exception as ex:
        cost = 0.00
        pass
    
    cursor.execute('''INSERT INTO stima(value, imageurl, date, cost)
                        VALUES(?,?,?,?)''', (text,value,date, cost))
   
    # never forget this, if you want the changes to be saved:
    connection.commit()
    return text
if __name__ == '__main__':
    print(getOCR())