from flavial_emotion_recognition import EmotionRecognition
import cv2

# Initialize emotion recognition model
er = EmotionRecognition(device='cpu')

# Open webcam (0 is default camera, 1 is usually external camera)
cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()
    if not success:
        break

    # Run emotion recognition
    frame = er.recognise_emotion(frame, return_type='BGR')

    # Show the frame
    cv2.imshow("Frame", frame)

    # Exit on ESC key
    key = cv2.waitKey(1)
    if key == 27:
        break

# Release resources
cam.release()
cv2.destroyAllWindows()
