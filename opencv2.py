import cv2
import random

img = cv2.imread('pic/pic2.jpg', -1)
# print(img.shape)

# Copy part of image
# y:500-700 x:600-900
tag = img[500:700, 600:900]
# Replace
img[100:300, 650:950] = tag

# Change first 100 rows to random pixels
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Changed One', img)
cv2.waitKey(0)
cv2.destroyAllWindows()