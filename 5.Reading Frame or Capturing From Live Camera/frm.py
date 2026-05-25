#Reading frame from camera – video streaming

import cv2

# Open the camera (0 = default webcam,1= external camera)
vs = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, img = vs.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    # Show the frame
    cv2.imshow("VideoStream", img)

    # Exit when 'q' is pressed
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Release resources
vs.release()
cv2.destroyAllWindows()
