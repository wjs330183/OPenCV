import time

import cv2

cv2.namedWindow("left")
cv2.namedWindow("right")
# 获取摄像头
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(2)
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# 打开摄像头
# cap.open(1)

while cap1.isOpened():
    # 获取画面
    flag, frame1 = cap1.read()
    flag, frame2 = cap2.read()

    ######################画面处理1##########################
    # 灰度图
    # frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    # frame = cv2.medianBlur(frame, 5)
    # img_blur = cv2.GaussianBlur(frame, ksize=(21, 21),
    #                             sigmaX=0, sigmaY=0)
    # frame = cv2.divide(frame, img_blur, scale=255)

    left_frame = frame1
    right_frame = frame2
    # right_frame = frame[0:720, 1280:2560]
    cv2.imshow("left", left_frame)
    cv2.imshow("right", right_frame)
    now = time.time()

    # 画面显示
    # cv2.imshow('mytest', frame)
    # 设置退出按钮
    key_pressed = cv2.waitKey(100)
    print('单机窗口，输入按键，电脑按键为', key_pressed, '按esc键结束')
    if key_pressed == 27:
        break

# 关闭摄像头
cap1.release()
# 关闭图像窗口
cv2.destroyAllWindows()
