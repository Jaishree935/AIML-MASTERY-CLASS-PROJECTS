import cv2

# Read the image
img = cv2.imread(r"C:/Users/jaish/Desktop/AIML/Threshold Value/img.png")

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # Convert to grayscale
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    gaussBlur = cv2.GaussianBlur(grayImg, (21, 21), 0)

    # Apply threshold [1] --> it show image, [0] --> It show its value
    thresholdImg = cv2.threshold(grayImg, 150, 255, cv2.THRESH_BINARY)[1]

    # Save the thresholded image
    cv2.imwrite("threshold.jpg", thresholdImg)

    # Optional: show results
    cv2.imshow("Gray", grayImg)
    cv2.imshow("GaussianBlur", gaussBlur)
    cv2.imshow("Threshold", thresholdImg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
