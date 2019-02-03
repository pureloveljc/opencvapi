#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-3 下午3:57"
# svm本质　寻求一个最优的超平面　　分类
# svm 核：svm分类器
import cv2
import numpy as np
import matplotlib.pyplot as plt
# 1 数据准备

rand1 = np.array([[155, 48], [159, 50], [164, 53], [168, 56], [172, 60]])  # 女生
rand2 = np.array([[152, 53], [156, 55], [160, 56], [172, 64], [176, 65]])  # 男生

label = np.array([[0], [0], [0], [0], [0], [1], [1], [1], [1], [1]])

data = np.vstack((rand1, rand2))
data = np.array(data, dtype=np.float32)

# 　训练
svm = cv2.ml.SVM_create()   # ml机器学习模块
# 属性设置
svm.setType(cv2.ml.SVM_C_SVC)
svm.setKernel(cv2.ml.SVM_LINEAR)
svm.setC(0.01)

result = svm.train(data, cv2.ml.ROW_SAMPLE, label)

# 预测
pt_data = np.vstack([[167, 55], [180, 87]])
pt_data = np.array(pt_data, np.float32)
print(pt_data)
par1, par2 = svm.predict(pt_data)
print(par1)
print(par2)