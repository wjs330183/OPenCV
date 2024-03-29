import cv2
import numpy as np

# # 左相机内参
# left_camera_matrix = np.array([[0.0, 0.0, 0.0],
#                                [0.0, 0.0, 0.0],
#                                [0.0, 0.0, 0.0]])
# left_camera_matrix = np.array([[1918.336647435351, 0.0, 1493.349665689275],
#                                [0.0, 1929.424204942624, 913.0624321772135],
#                                [0.0, 0.0, 1.0]])
# 左相机内参
left_camera_matrix = np.array([[1918.336647435351, 0.0, 0.0],
                               [0.0, 1929.424204942624, 0.0],
                               [1493.349665689275, 913.0624321772135, 1.0]])

# 左相机畸变系数:[k1, k2, p1, p2, k3]
left_distortion = np.array([[0.102971189677152, -0.150513236446186, 0, 0, 0]])
# left_distortion = np.array([[0, 0, 0, 0, 0]])
#
# # 右相机内参
# right_camera_matrix = np.array([[0.0, 0.0, 0.0],
#                                 [0.0, 0.0, 0.0],
#                                 [0.0, 0.0, 0.0]])
# right_camera_matrix = np.array([[1921.220771836132, 0.0, 1397.748936353007],
#                                 [0.0, 1933.968436925682, 920.7554871734869],
#                                 [0.0, 0.0, 1.]])
# 右相机内参
right_camera_matrix = np.array([[1921.220771836132, 0.0, 0.0],
                                [0.0, 1933.968436925682, 0.0],
                                [1397.748936353007, 920.7554871734869, 1.0]])

# 右相机畸变系数:[k1, k2, p1, p2, k3]
right_distortion = np.array([[0.061692821469276, -0.070543947538391, -0.00133793245429668, -0.00188957913931929, 0]])
# right_distortion = np.array([[0, 0, 0, 0, 0]])

# om = np.array([-0.00009, 0.02300, -0.00372])
# R = cv2.Rodrigues(om)[0]

# R = np.array([[0.999948733569707, -0.0002552474919995824, -0.0002552474919995824],
#               [0.0003688166270061849,0.999936994871616, -0.011219191656178],
#               [-0.010119002254927, 0.011222349835941, 0.999885825810890]])
# # 旋转矩阵
R = np.array([[0.999948733569707, 0.0003688166270061849, -0.010119002254927],
              [-0.0002552474919995824, 0.999936994871616, 0.00439412154902114],
              [0.010122503695104, -0.011219191656178, 0.999885825810890]])

# R = np.array([[0.0, 0.0, 0.0],
#               [0.0, 0.0, 0.0],
#               [0.0, 0.0, 0.0]])

# 平移向量
T = np.array([22.466287171260824, -0.261764990785632, -0.422860620724262])
# T = np.array([0, 0, 0])

size = (640, 480)  # 图像尺寸

R1, R2, P1, P2, Q, validPixROI1, validPixROI2 = cv2.stereoRectify(left_camera_matrix, left_distortion,
                                                                  right_camera_matrix, right_distortion, size, R,
                                                                  T)

left_map1, left_map2 = cv2.initUndistortRectifyMap(left_camera_matrix, left_distortion, R1, P1, size, cv2.CV_16SC2)
right_map1, right_map2 = cv2.initUndistortRectifyMap(right_camera_matrix, right_distortion, R2, P2, size, cv2.CV_16SC2)
