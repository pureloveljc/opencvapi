#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 下午3:39"
import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Picture_beautification/damaged.jpg', 1)
height = img.shape[0]
width = img.shape[1]
dst = cv2.GaussianBlur(img, (5, 5), 1.5)  # 高斯滤波 滤波后的图像大小不变。  和卷积区别
cv2.imshow('dst', dst)
cv2.waitKey(0)

