
import cv2
import imutils

# Corrected path (note 'jaish' instead of 'jais')
img = cv2.imread(r"C:/Users/jaish/Desktop/AIML/Resize an image/img.png")

if img is None:
    print("Error: Could not load image. Check the path and file name.")
else:
    resizeimg = imutils.resize(img, width=100)
    cv2.imshow('Original', img)
    cv2.imshow('Resized', resizeimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
