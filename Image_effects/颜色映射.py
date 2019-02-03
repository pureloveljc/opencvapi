#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 下午8:36"

import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
height = img.shape[0]
width = img.shape[1]
dst = np.zeros((height, width, 3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
        b, g, r = img[i, j]
        b = b*1.5
        g = g*1.3
        if b > 255:
            b = 255
        if g > 255:
            g = 255
        dst[i, j] = b, g, r
cv2.imshow('dst', dst)
cv2.waitKey(0)
