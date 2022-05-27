import cv2 as cv
import copy
import numpy as np


def edge_demo(image):
    blurred1 = cv.GaussianBlur(image, (5, 5), 0)
    blurred = cv.GaussianBlur(blurred1, (3, 3), 0)
    cv.imshow("Canny_edge_blurred", blurred)

    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # 求X方向上的梯度
    grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
    # 求y方向上的梯度
    grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
    # 将梯度值转化到8位上来
    x_grad = cv.convertScaleAbs(grad_x)
    y_grad = cv.convertScaleAbs(grad_y)
    # 将两个梯度组合起来
    src1 = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
    # 组合梯度用canny算法，其中50和100为阈值40, 170
    edge = cv.Canny(blurred, 40, 170)
    cv.imshow("Canny_edge_1", edge)
    edge1 = cv.Canny(grad_x, grad_y, 10, 50)
    height = edge1.shape[0]
    width = edge1.shape[1]
    existList = []
    colsList = []
    rowsList = []

    for row in range(height):
        rowsList.clear()
        for col in range(width):
            array = edge1.item(row, col)
            edge1.item(row, col)
            rowsList.append(array)
        existList.append(copy.deepcopy(rowsList))
    #
    # for row in range(width):
    #     colsList.clear()
    #     for col in range(height):
    #         array = edge1.item(col, row)
    #         colsList.append(array)
    #     existList.append(copy.deepcopy(colsList))
    kernel = np.ones((5, 5), np.uint8)
    hi_mask = cv.dilate(edge1, kernel, iterations=1)
    specular = cv.inpaint(src, hi_mask, 5, flags=cv.INPAINT_TELEA)
    cv.imshow("edge1", edge1)
    cv.imshow("specular", specular)

    # 用边缘做掩模，进行bitwise_and位运算
    edge2 = cv.bitwise_and(image, image, mask=edge)
    cv.imshow("bitwise_and", edge2)
    # height = edge2.shape[0]
    # width = edge2.shape[1]
    # channels = edge2.shape[2]
    # print("width: %s  height: %s  channels: %s"%(width, height, channels))
    # for row in range(height):
    #     for col in range(width):
    #         for c in range(channels):
    #             pv = image[row, col, c]  # 获取每个像素点的每个通道的数值
    #             image[row, col, c] = 255 - pv  # 灰度值是0-255   这里是修改每个像素点每个通道灰度值

    print("end")


src = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
cv.imshow("part", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
