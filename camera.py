import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture the video frame by frame
    ret, frame = cap.read()

    # convert to gray picture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the picture
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# release the capture when quit
cap.release()
cv2.destroyAllWindows()
