import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Change to the two extremes of the color range set by hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    pick_colour1 = np.array([0, 0, 0])
    pick_colour2 = np.array([254, 237, 88])

    # Colors in two ranges
    pick = cv2.inRange(hsv, pick_colour1, pick_colour2)
    result = cv2.bitwise_and(frame, frame, mask=pick)

    # Show selected colors
    cv2.imshow('frame', result)
    # A white display of the selected color
    cv2.imshow('picked colour => white', pick)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
