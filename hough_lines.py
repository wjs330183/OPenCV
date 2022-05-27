import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import copy




def edge_demo(image):
    blurred1 = cv.GaussianBlur(image, (3, 3), 0)
    # blurred = cv.GaussianBlur(blurred1, (3, 3), 0)

    GrayImage = cv.cvtColor(blurred1, cv.COLOR_BGR2GRAY)
    retval, dst = cv.threshold(GrayImage, 85, 255, cv.THRESH_BINARY)
    cv.imshow("bitwise_and", dst)
    height = dst.shape[0]
    width = dst.shape[1]
    # channels = dst.shape[2]
    print("width: %s  height: %s " % (width, height))
    sum_list = []
    exist_list = []
    part_exist_list = []
    white_miss_list = []
    black_miss_list = []
    part_miss_list = []
    row_list = []
    # 获取零件存在最小范围
    for row in range(height):
        row_list.clear()
        for col in range(width):
            array = dst.item(row, col)
            row_list.append(array)
        white_count = row_list.count(255)
        black_count = row_list.count(0)
        if white_count > (0.9 * width):
            white_miss_list.append(copy.deepcopy(row_list))
        elif black_count > (0.5 * width):
            black_miss_list.append(copy.deepcopy(row_list))
        else:
            exist_list.append(copy.deepcopy(row_list))
    # 判断是否有零件
    if len(exist_list) < 240:
        print("miss")

    if len(black_miss_list) > 0:
        black_miss_image = np.asarray(black_miss_list, np.uint8)
        cv.imshow("black_miss_image", black_miss_image)

    if len(white_miss_list) > 0:
        white_miss_image = np.asarray(white_miss_list, np.uint8)
        cv.imshow("white_miss_image", white_miss_image)

    if len(exist_list) > 0:
        exist_image = np.asarray(exist_list, np.uint8)
        cv.imshow("exist_image", exist_image)

    for exist in exist_list:
        count = exist.count(0)
        if count > (0.5 * height):
            part_miss_list.append(copy.deepcopy(exist))
        else:
            part_exist_list.append(copy.deepcopy(exist))

    part_miss_image = np.asarray(part_miss_list, np.uint8)
    cv.imshow("part_miss_image", part_miss_image)

    sum_black = []
    sum = 0
    for artExist in part_exist_list:
        count = artExist.count(0)
        sum = sum + count
        sum_black.append(copy.deepcopy(count))

    part_exist_image = np.asarray(part_exist_list, np.uint8)
    # cv.imshow("partExistImage", part_exist_image)

    if len(part_exist_list) != 0:
        percent = sum / (len(part_exist_list) * 1000)
    else:
        percent = 0

    if float(0.15) < percent < float(0.30):
        print("percent = " + percent.__str__() + "--------->exist")
    else:
        print("percent = " + percent.__str__() + "--------->miss")



img = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
blurred = cv.GaussianBlur(img, (3, 3), 0)
gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
# 求X方向上的梯度
grad_x = cv.Sobel(gray, cv.CV_16SC1, 1, 0)
# 求y方向上的梯度
grad_y = cv.Sobel(gray, cv.CV_16SC1, 0, 1)
# 将梯度值转化到8位上来
x_grad = cv.convertScaleAbs(grad_x)
y_grad = cv.convertScaleAbs(grad_y)
# 将两个梯度组合起来
src = cv.addWeighted(x_grad, 0.5, y_grad, 0.5, 0)
edge = cv.Canny(src, 40, 170)
cv.imshow("edge", edge)

edges = cv.Canny(blurred, 40, 170)
# plt.imshow(edges, cmap=plt.cm.gray)
cv.imshow("edges", edges)

lines = cv.HoughLines(edges, 0.9, np.pi / 180, 150)
i = 0
for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = rho * a
    y0 = rho * b
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * a)
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * a)
    if (i == 6):
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))
    elif(i == 4):
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))
    elif(i == 7):
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))
    elif(i == 11):
        cv.line(img, (x1, y1), (x2, y2), (0, 255, 0))
    i = i + 1

# points1 = np.float32([[207, 151], [517, 285], [17, 601], [343, 731]])
points1 = np.float32([[2, 367], [997, 331], [2, 612], [997, 576]])
points2 = np.float32([[2, 367], [997, 367], [2, 612], [997, 612]])
# points2 = np.float32([[2, int(367 * 0.9986295)], [997, 331], [2, int(612 * 0.9986295)], [997, 576]])
# points2 = np.float32([[207, 151], [517, int(285 * 0.9986295)], [17, 601], [343, int(731 * 0.9986295)]])

M = cv.getPerspectiveTransform(points1, points2)

Perspective_img = cv.warpPerspective(img, M, (0, 0))
cv.imshow("Perspective_img", Perspective_img)
edge_demo(Perspective_img)
# plt.imshow(img[:, :, ::-1])
cv.imshow("img", img)
cv.waitKey(0)
cv.destroyAllWindows()
