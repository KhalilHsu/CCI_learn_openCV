import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # draw line The upper left corner is（0，0）
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    # draw rectangle
    img = cv2.rectangle(img, (500, 500), (200, 200), (210, 210, 210), 5)
    # circle
    img = cv2.circle(img, (1200, 300), 60, (0, 0, 255), -1)
    # words
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'CCI is COOL!', (10, height - 10), font, 2, (250, 250, 0), 5, cv2.LINE_AA)

    cv2.imshow('Draw Test', img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
