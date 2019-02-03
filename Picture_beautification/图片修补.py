#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 上午11:57"

import cv2
import numpy as np

# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# for i in range(200, 300):
#     img[i, 200] = (255, 255, 255)
#     img[i, 200 + 1] = (255, 255, 255)
#     img[i, 200 - 1] = (255, 255, 255)
# for i in range(150, 250):
#     img[250, i] = (255, 255, 255)
#     img[250 + 1, i] = (255, 255, 255)
#     img[250 - 1, i] = (255, 255, 255)
# cv2.imwrite('damaged.jpg', img)
# cv2.imshow('image', img)
# cv2.waitKey(0)

# 1 坏图 2 array修补区域 3 inpaint
img = cv2.imread('damaged.jpg', 1)
cv2.imshow('src', img)
imgInfo = img.shape
height = imgInfo[0]
width = imgInfo[1]
paint = np.zeros((height, width, 1), np.uint8)

for i in range(200, 300):
    paint[i, 200] = 255
    paint[i, 200 + 1] = 255
    paint[i, 200 - 1] = 255
for i in range(150, 250):
    paint[250, i] = 255
    paint[250 + 1, i] = 255
    paint[250 - 1, i] = 255
cv2.imshow('paint', paint)
# 1 src 2 mask
imgDst = cv2.inpaint(img, paint, 3, cv2.INPAINT_TELEA)

cv2.imshow('image', imgDst)
cv2.waitKey(0)
