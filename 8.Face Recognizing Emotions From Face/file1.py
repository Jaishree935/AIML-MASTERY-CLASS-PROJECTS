import urllib.request
import numpy as np
import cv2
import imutils

url = 'http://192.168.1.37:8080/shot.jpg'

while True:
    # Read image from URL
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    
    # Decode image
    frame = cv2.imdecode(imgNp, -1)
    
    # Resize frame
    frame = imutils.resize(frame, width=450)
    
    # Show frame
    cv2.imshow("Frame", frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
