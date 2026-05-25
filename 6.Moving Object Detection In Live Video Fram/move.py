import cv2
import imutils

# Open camera (0 = default webcam, 1 = external camera)
cam = cv2.VideoCapture(0)

firstFrame = None
area = 500

while True:
    # Read frame
    ret, img = cam.read()
    if not ret:
        print("Failed to grab frame")
        break

    text = "Normal"

    # Resize for consistency
    img = imutils.resize(img, width=500)

    # Convert to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    gaussianImg = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # Capture first frame as reference
    if firstFrame is None:
        firstFrame = gaussianImg
        continue

    # Compute absolute difference between current frame and first frame
    imgDiff = cv2.absdiff(firstFrame, gaussianImg)

    # Threshold the difference
    threshImg = cv2.threshold(imgDiff, 25, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes
    threshImg = cv2.dilate(threshImg, None, iterations=2)

    # Find contours
    cnts = cv2.findContours(threshImg.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < area:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        text = "Moving Object detected"

    # Print status
    print(text)

    # Put text on frame
    cv2.putText(img, text, (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Show video feed
    cv2.imshow("cameraFeed", img)

    # Exit when 'q' is pressed
    key = cv2.waitKey(10) & 0xFF
    if key == ord("q"):
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
