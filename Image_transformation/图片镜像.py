#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午5:21"

import numpy as np
import cv2
# 图片镜像
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)
cv2.imshow('src', img)
height = img.shape[0]
weight = img.shape[1]
dst = np.zeros((height*2, weight, 3), np.uint8)
for i in range(height):
    for j in range(weight):
        dst[i, j] = img[i, j]
        # x 不变
        dst[height*2-i-1, j] = img[i,j]
for i in range(weight):
    dst[height, i] = (0, 0, 255) #BGR
cv2.imshow('dst', dst)
cv2.waitKey(0)