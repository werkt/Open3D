# Open3D: www.open3d.org
# The MIT License (MIT)
# See license file or visit www.open3d.org for details

# examples/Python/Tutorial/Basic/pointcloud.py

import numpy as np
from open3d import *

def display_inlier_outlier(cloud,ind):
    inlier_cloud = select_down_sample(cloud,ind)
    outlier_cloud = select_down_sample(cloud,ind,True)

    outlier_cloud.paint_uniform_color([0.1, 0.9, 0.1])
    inlier_cloud.paint_uniform_color([0.9, 0.1, 0.1])
    print("Showing outliers: ")
    draw_geometries([outlier_cloud])

    print("Showing inliers: ")
    draw_geometries([inlier_cloud])

    print("Showing both sets together: ")
    draw_geometries([inlier_cloud,outlier_cloud])

if __name__ == "__main__":

    print("Load a ply point cloud, print it, and render it")
    pcd = read_point_cloud("../../TestData/fragment.ply")
    print(pcd)
    print(np.asarray(pcd.points))
    draw_geometries([pcd])

    print("Downsample the point cloud with a voxel of 0.05")
    downpcd = voxel_down_sample(pcd, voxel_size = 0.05)
    draw_geometries([downpcd])

    print("Recompute the normal of the downsampled point cloud")
    estimate_normals(downpcd, search_param = KDTreeSearchParamHybrid(
            radius = 0.1, max_nn = 30))
    draw_geometries([downpcd])

    print("Print a normal vector of the 0th point")
    print(downpcd.normals[0])
    print("Print the normal vectors of the first 10 points")
    print(np.asarray(downpcd.normals)[:10,:])
    print("")

    print("Load a polygon volume and use it to crop the original point cloud")
    vol = read_selection_polygon_volume("../../TestData/Crop/cropped.json")
    chair = vol.crop_point_cloud(pcd)
    draw_geometries([chair])
    print("")

    print("Paint chair")
    chair.paint_uniform_color([1, 0.706, 0])
    draw_geometries([chair])
    print("")

    print("------ Statistical Oulier Removal -------")
    cl,ind = statistical_outlier_removal(pcd,50,2)
    display_inlier_outlier(pcd,ind)

    print("------ Radius Oulier Removal -------")
    cl,ind = radius_outlier_removal(pcd,60,0.05)
    display_inlier_outlier(pcd,ind)