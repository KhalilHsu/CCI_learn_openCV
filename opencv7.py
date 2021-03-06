import cv2

img = cv2.resize(cv2.imread('pic/messi.jpg', 0), (0, 0), fx=0.4, fy=0.4)
template = cv2.resize(cv2.imread('pic/ball.jpg', 0), (0, 0), fx=0.4, fy=0.4)

# (height and width)
h, w = template.shape

# Try as many ways as possible to match
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    # 把template图像按照原始大小，从左上开始以单位像素为大小扫描对比，记录每次对比的相似度，最终得出结果。
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    # Display a check box on the picture around the matching image
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match Result', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
