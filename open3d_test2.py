import numpy as np
import open3d as o3d
import h5py


def load_h5(h5_filename):
    f = h5py.File(h5_filename)
    point_map = f['point_map'][:]
    intrinsics = f['intrinsics'][:]
    return (point_map, intrinsics)


datas, labels = load_h5("/Users/json/Documents/point_cloud_compression/point_cloud.h5")

bunny_pcd = o3d.geometry.PointCloud()
points = datas[0][..., 0:3]
bunny_pcd.points = o3d.utility.Vector3dVector(points)

point = np.asarray(bunny_pcd.points)
N = point.shape[0]
# 点云随机着色
colors = bunny_pcd.colors = o3d.utility.Vector3dVector(np.random.uniform(0, 1, size=(N, 3)))
# 可视化点云
o3d.visualization.draw_geometries([bunny_pcd], window_name="原始点云",
                                  width=1024, height=768,
                                  left=50, top=50,
                                  mesh_show_back_face=False)
# 创建八叉树
octree = o3d.geometry.Octree(max_depth=8)
# 从点云中构建八叉树
octree_datas = octree.convert_from_point_cloud(bunny_pcd, size_expand=0.01)
# 可视化八叉树
o3d.visualization.draw_geometries([octree], window_name="可视化八叉树",
                                  width=1024, height=768,
                                  left=50, top=50,
                                  mesh_show_back_face=False)
