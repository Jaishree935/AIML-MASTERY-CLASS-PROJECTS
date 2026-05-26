import cv2

# Load Haar cascade file (make sure the XML file is in your working directory)
alg = "C:/Users/jaish/Desktop/AIML/Haar Cascade FrontalFace Algorithm/haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)

# Initialize camera (0 = default webcam, 1 = external camera)
cam = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Convert to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = haar_cascade.detectMultiScale(grayImg, scaleFactor=1.3, minNeighbors=4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    # Show video feed
    cv2.imshow("Face Detection", img)

    # Exit when ESC key is pressed
    key = cv2.waitKey(10) & 0xFF
    if key == 27:  # ESC key
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
