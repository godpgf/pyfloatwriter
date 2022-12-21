import numpy as np
import glob
import os
import scipy.io

basis3dmm = scipy.io.loadmat("../face2dto3d/hifi3dface/3DMM/files/AI-NEXT-Shape.mat")
basis3dmm['keypoints'] = np.squeeze(basis3dmm['keypoints'])

# 平均形状
mu_shape = basis3dmm["mu_shape"]
# 多个基础形状
basis_shape = basis3dmm["basis_shape"]
# 多个基础表情
basis_exp = basis3dmm["basis_exp"]
# uv
vt = basis3dmm['vt_list']
# 三角面片
tri = basis3dmm['tri']

print(mu_shape.shape, basis_shape.shape, basis_exp.shape, vt.shape, tri.shape)

from pywriter import PYWriter
PYWriter.writer_float_array(mu_shape, "mu_shape_61443.bat")
PYWriter.writer_float_array(basis_shape, "basis_shape_500_61443.bat")
PYWriter.writer_float_array(basis_exp, "basis_exp_199_61443.bat")
PYWriter.writer_float_array(vt, "vt_20792_2.bat")
PYWriter.writer_int_array(tri, "tri_18684_3.bat")
print("finish")
