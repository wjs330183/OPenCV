import cv2 as cv
import numpy
import numpy as np
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


src = cv.imread("/Users/json/Downloads/image/Sat Apr 30 14-00-28 2022 _1.jpg")
cv.imshow("part", src)
edge_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
