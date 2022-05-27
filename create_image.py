import cv2 as cv
import numpy as np
import copy


def create_image(image):
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
    edge = cv.Canny(src1, 40, 120)
    cv.imshow("Canny_edge_1", edge)
    edge1 = cv.Canny(grad_x, grad_y, 10, 50)

    cv.imshow("edge", edge)
    existList = improve_image(edge)

    part_exist_image = np.asarray(existList, np.uint8)

    existList1 = improve_image(part_exist_image)
    part_exist_image1 = np.asarray(existList1, np.uint8)

    existList2 = connect_image(part_exist_image1, 10, 35)
    part_exist_image2 = np.asarray(existList2, np.uint8)

    img_flip = cv.transpose(part_exist_image)
    img_flip1 = cv.transpose(part_exist_image2)

    cv.imshow("partExistImage", img_flip)
    cv.imshow("partExistImage1", part_exist_image1)
    cv.imshow("partExistImage2", img_flip1)


def improve_image(image):
    height = image.shape[0]
    width = image.shape[1]
    existList = []
    rowsList = []
    for col in range(width):
        rowsList.clear()
        for row in range(height):
            array = image.item(row, col)
            if 1 < col < (width - 1):
                if 1 < row < (height - 1):
                    array_bottom_left = image.item(row + 1, col - 1)
                    array_bottom_right = image.item(row + 1, col + 1)
                    array_upper_left = image.item(row - 1, col - 1)
                    array_upper_right = image.item(row - 1, col + 1)
                    if array_bottom_left == 255 | array_bottom_right == 255:
                        rowsList.append(255)
                    elif array_upper_left == 255 | array_upper_right == 255:
                        rowsList.append(255)
            if row > len(rowsList):
                rowsList.append(copy.deepcopy(array))
        existList.append(copy.deepcopy(rowsList))
    return existList


def connect_image(image, distance_min, distance_max):
    height = image.shape[0]
    width = image.shape[1]
    exist_list = []
    rows_list = []
    for col in range(width):
        rows_list.clear()
        for row in range(height):
            array = image.item(row, col)
            if 1 < col < (width - 1):
                if 1 < row < (height - 1):
                    if array == 255:
                        array_bottom = image.item(row + 1, col)
                        if array_bottom == 0:
                            array_next_list = []
                            for row_next in range(distance_max):
                                row_max = row + row_next + 1
                                if row_max > (height - 1):
                                    break
                                array_next = image.item(row_max, col)
                                array_next_list.append(255)
                                if array_next == 255:
                                    if row_next > distance_min:
                                        rows_list.append(array)
                                        rows_list.extend(copy.deepcopy(array_next_list))
                                        row = row + len(array_next_list)
                                        # if len(array_next_list) > 10:
                                        #     print("succeed")
                                    break
            if row > len(rows_list):
                rows_list.append(array)
        exist_list.append(copy.deepcopy(rows_list))
    return exist_list


src = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
cv.imshow("part", src)
create_image(src)  # 调用创建图片的函数
cv.waitKey(0)  # 保持界面框
cv.destroyAllWindows()
