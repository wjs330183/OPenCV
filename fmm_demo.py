import cv2 as cv
import numpy as np
import copy


def fmm_demo(image):
    hight, width, depth = src.shape[0:3]
    blurred = cv.GaussianBlur(image, (3, 3), 0)

    # 图片二值化处理，把[240, 240, 240]~[255, 255, 255]以外的颜色变成0
    thresh = cv.inRange(blurred, np.array([0, 0, 0]), np.array([55, 55, 55]))

    part_miss_image = improve_image(thresh)
    # cv.imshow("part_miss_image", part_miss_image)

    # 创建形状和尺寸的结构元素
    # kernel为一个5x5的，元素均为1，类型为uint8的矩阵
    kernel = np.ones((3, 3), np.uint8)

    # 扩张待修复区域
    hi_mask = cv.dilate(thresh, kernel, iterations=1)
    specular = cv.inpaint(src, hi_mask, 5, flags=cv.INPAINT_TELEA)

    cv.namedWindow("Image", 0)
    cv.resizeWindow("Image", int(width), int(hight))
    cv.imshow("Image", src)

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


def improve_image(image):
    height = image.shape[0]
    width = image.shape[1]
    height_threshold = int(0.9 * height)
    width_threshold = int(0.8 * width)
    exist_list = []
    row_list = []
    miss_list = []
    for row in range(height):
        row_list.clear()
        for col in range(width):
            array = image.item(row, col)
            row_list.append(array)
        white_count = row_list.count(0)
        black_count = row_list.count(255)
        if black_count > width_threshold | white_count > width_threshold:
            miss_list.append(copy.deepcopy(row_list))
        else:
            exist_list.append(copy.deepcopy(row_list))

    exist_image = np.asarray(exist_list, np.uint8)
    miss_image = np.asarray(miss_list, np.uint8)
    cv.imshow("exist_image", exist_image)
    cv.imshow("miss_image", miss_image)

    return exist_image


# src = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
src = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-34 2022 _1.jpg")
cv.imshow("part", src)
fmm_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
