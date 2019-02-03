#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午3:58"

import cv2
import numpy as np
# 剪切 x 100->200  y 100->300

# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# img_height = img.shape[0]
# img_weight = img.shape[1]
#
# dst = img[100:500, 100:800]
# cv2.imshow('image', dst)
# cv2.waitKey(0)


# 位移 1api 2 算法原理 3源代码
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# cv2.imshow('image', img)
# img_height = img.shape[0]
# img_weight = img.shape[1]
# # 设置平移矩阵
# matShift = np.array([[1, 0, 100], [0, 1, 200]], dtype=np.float32)
# dst = cv2.warpAffine(img, matShift, (img_height, img_weight))
# cv2.imshow('image1', dst)
# cv2.waitKey(0)

# 矩阵拆分 [1,0,100] [0, 1,200]

# 位移源码

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
cv2.imshow('image', img)
img_height = img.shape[0]
img_weight = img.shape[1]
dst = np.zeros(img.shape, np.uint8)

for i in range(img_height):
    for j in range(img_weight-100):
        dst[i, j+100] = img[i, j]
cv2.imshow('image1', dst)
cv2.waitKey(0)

# # 设置平移矩阵
# matShift = np.array([[1, 0, 100], [0, 1, 200]], dtype=np.float32)
# dst = cv2.warpAffine(img, matShift, (img_height, img_weight))
# cv2.imshow('image1', dst)
# cv2.waitKey(0)