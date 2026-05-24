import cv2

# Read the image (make sure the path is correct)
image = cv2.imread(r"C:/Users/jaish/Desktop/AIML/img.png")

# Check if image is loaded properly
if image is None:
    print("Error: Image not found at the given path.")
else:
    # Convert to grayscale
    grayimage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show images
    cv2.imshow('Original', image)
    cv2.imshow('Gray', grayimage)

    # Save grayscale image
    cv2.imwrite('graynew.png', grayimage)

    # Keep window open until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
