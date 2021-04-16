import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # get the length and width data of cap
    width = int(cap.get(3))
    height = int(cap.get(4))

    # create an array to store four camera images
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
    # Upper left
    image[:height // 2, :width // 2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # Lower left
    image[height // 2:, :width // 2] = smaller_frame
    # Upper right
    image[:height // 2, width // 2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # Lower right
    image[height // 2:, width // 2:] = smaller_frame

    # Display a picture of the camera
    cv2.imshow('this is the camera', image)

    # Press Q to exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
