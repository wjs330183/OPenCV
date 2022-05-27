import cv2 as cv
import numpy as np

img = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
cv.imshow("img", img)

result3 = img.copy()

img = cv.GaussianBlur(img, (3, 3), 0)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

edges = cv.Canny(gray, 50, 150, apertureSize=3)
# cv.imwrite("/Users/json/Downloads/image/canny.jpg", edges)

src = np.float32([[207, 151], [517, 285], [17, 601], [343, 731]])
dst = np.float32([[0, 0], [337, 0], [0, 488], [337, 488]])
m = cv.getPerspectiveTransform(src, dst)
result = cv.warpPerspective(result3, m, (0, 0))
cv.imshow("result", result)
cv.waitKey(0)
