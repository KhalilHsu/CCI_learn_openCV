import cv2

# -1, 0, 1 Show different color modes
img = cv2.imread('pic/pic1.jpg', -1)

# Resize the ima
# img = cv2.resize(img,(800,500))
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.2)

# rotate pic
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE)

# write and show pic
cv2.imwrite('pic/this is how write img1.jpg', img)
cv2.imshow('This is the label of the windows', img)

# Waiting time, run the next line of code, 0 and 1 have different meanings.
cv2.waitKey(0)
cv2.destroyAllWindows()
