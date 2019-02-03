#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午6:45"

import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)
height = img.shape[0]
weight = img.shape[1]

matRotate = cv2.getRotationMatrix2D((height*0.5, weight*0.5), 45, 0.5)  # 缩放系数

dst = cv2.warpAffine(img, matRotate, (height, weight))
cv2.imshow('dst', dst)
cv2.waitKey(0)