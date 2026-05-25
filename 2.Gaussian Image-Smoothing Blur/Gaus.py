import cv2

# Use raw string (r"...") or forward slashes
img = cv2.imread(r"C:/Users/jaish/Desktop/AIML/Gaussiam Image/img.png")

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    # Apply Gaussian Blur with different kernels
    gaussianImg = cv2.GaussianBlur(img, (41, 41), 50)
    gaussianImg1 = cv2.GaussianBlur(img, (21, 21), 0)

    # Show results
    cv2.imshow("Original", img)
    cv2.imshow("GaussianBlur", gaussianImg)
    cv2.imshow("GaussianBlur1", gaussianImg1)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
