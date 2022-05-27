import cv2 as cv
import numpy as np

path = "/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg"

img = cv.imread(path)
hight, width, depth = img.shape[0:3]

#图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
thresh = cv.inRange(img, np.array([0, 0, 0]), np.array([130, 130, 130]))

#创建形状和尺寸的结构元素
#kernel为一个5x5的，元素均为1，类型为uint8的矩阵
kernel = np.ones((5, 5), np.uint8)

#扩张待修复区域
hi_mask = cv.dilate(thresh, kernel, iterations=1)
specular = cv.inpaint(img, hi_mask, 5, flags=cv.INPAINT_TELEA)

cv.namedWindow("Image", 0)
cv.resizeWindow("Image", int(width), int(hight))
cv.imshow("Image", img)

cv.namedWindow("thresh", 0)
cv.resizeWindow("thresh", int(width), int(hight))
cv.imshow("thresh", thresh)

cv.namedWindow("mask", 0)
cv.resizeWindow("mask", int(width), int(hight))
cv.imshow("mask", hi_mask)

cv.namedWindow("newImage", 0)
cv.resizeWindow("newImage", int(width), int(hight))
cv.imshow("newImage", specular)

cv.waitKey(0)
cv.destroyAllWindows()
