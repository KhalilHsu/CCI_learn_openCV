import cv2

cap = cv2.VideoCapture(0)
# 已经被训练好的
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    # gray is what opencv need
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # https://stackoverflow.com/questions/20801015/recommended-values-for-opencv-detectmultiscale-parameters
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)
    # rectangle xywh
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        # The eyes must be within the range of the face.(roi_gray)
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.05, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('Face and Eye Detection', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
