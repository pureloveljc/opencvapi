#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午6:30"

import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)
height = img.shape[0]
weight = img.shape[1]

# 三点确定一个平面 src 3 ->dst 3
matSrc = np.float32([[0, 0], [0, height-1], [weight-1, 0]])
matDst = np.float32([[50, 50], [200, height-200], [weight-300, 100]])
# 组合
matAffine = cv2.getAffineTransform(matSrc, matDst)  #

dst = cv2.warpAffine(img, matAffine, (weight, height))
cv2.imshow('dst', dst)
cv2.imwrite('image5.png', dst, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 0-9 不牺牲图片质量 压缩比低
cv2.waitKey(0)
