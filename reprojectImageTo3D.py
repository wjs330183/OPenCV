import cv2
import numpy as np

cam1 = cv2.VideoCapture(0)  # 摄像头的ID不同设备上可能不同
cam2 = cv2.VideoCapture(2)  # 摄像头的ID不同设备上可能不同

def get_depth(self, disparity, Q, scale=1.0, method=False):
    """
    reprojectImageTo3D(disparity, Q),输入的Q,单位必须是毫米(mm)
    :param disparity: 视差图
    :param Q: 重投影矩阵Q=[[1, 0, 0, -cx]
                       [0, 1, 0, -cy]
                       [0, 0, 0,  f]
                       [1, 0, -1/Tx, (cx-cx`)/Tx]]
        其中f为焦距，Tx相当于平移向量T的第一个参数
    :param scale: 单位变换尺度,默认scale=1.0,单位为毫米
    :return depth:ndarray(np.uint16),depth返回深度图, 即距离
    """
    # 将图片扩展至3d空间中，其z方向的值则为当前的距离
    if method:
        points_3d = cv2.reprojectImageTo3D(disparity, Q)  # 单位是毫米(mm)
        x, y, depth = cv2.split(points_3d)
    else:
        # baseline = abs(camera_config["T"][0])
        baseline = 1 / Q[3, 2]  # 基线也可以由T[0]计算
        fx = abs(Q[2, 3])
        depth = (fx * baseline) / disparity
    depth = depth * scale
    # depth = np.asarray(depth, dtype=np.uint16)
    depth = np.asarray(depth, dtype=np.float32)
    return depth

    def show_3dcloud_for_open3d(self, frameL, frameR, points_3d):
        """
        使用open3d显示点云
        :param frameL:
        :param frameR:
        :param points_3d:
        :return:
        """
        if self.use_open3d:
            x, y, depth = cv2.split(points_3d)  # depth = points_3d[:, :, 2]
            self.open3d_viewer.show(color_image=frameL, depth_image=depth)

    def show_3dcloud_for_pcl(self, frameL, frameR, points_3d):
        """
        使用PCL显示点云
        :param frameL:
        :param frameR:
        :param points_3d:
        :return:
        """
        if self.use_pcl:
            self.pcl_viewer.add_3dpoints(points_3d, frameL)
            self.pcl_viewer.show()
