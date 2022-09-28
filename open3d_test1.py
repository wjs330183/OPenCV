import h5py
import numpy as np
from numpy.core.fromnumeric import reshape
import open3d as o3d
import matplotlib.pyplot as plt


def visualize_with_label(datas, label, window_name="open3d"):
    # assert cloud.shape[0] == label.shape[0]

    # labels = np.asarray(label)
    # max_label = labels.max()
    # colors = plt.get_cmap("tab20")(labels / (max_label if max_label > 0 else 1))
    cloud = datas[0][..., 0:3]

    pt = o3d.geometry.PointCloud()
    pt.points = o3d.utility.Vector3dVector(cloud)
    # pt.colors = o3d.utility.Vector3dVector(colors[:, :3])

    vis = o3d.visualization.Visualizer()
    vis.create_window(width=500, height=500)  # 创建窗口
    render_option: o3d.visualization.RenderOption = vis.get_render_option()  # 设置点云渲染参数
    render_option.background_color = np.array([255, 255, 255])  # 设置背景色（这里为黑色）
    render_option.point_size = 2.0  # 设置渲染点的大小
    vis.add_geometry(pt)  # 添加点云
    vis.run()
    # o3d.visualization.draw_geometries([pt], 'part of cloud', width=500, height=500)


def load_h5(h5_filename):
    f = h5py.File(h5_filename)

    point_map = f['point_map'][:]

    intrinsics = f['intrinsics'][:]
    return (point_map, intrinsics)


def load_h5_data_label_seg(h5_filename):
    f = h5py.File(h5_filename)

    point_map = f['point_map'][:]
    intrinsics = f['intrinsics'][:]
    seg = f['pid'][:]
    return (point_map, intrinsics, seg)


datas, labels = load_h5("/Users/json/Documents/point_cloud_compression/point_cloud.h5")

# one block
points = datas[0][..., 0:3]
label = labels[0]
visualize_with_label(datas, label)


