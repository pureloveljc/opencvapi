#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 上午10:09"

import cv2
import numpy as np
#
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
height = img.shape[0]
wdith = img.shape[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, wdith, 1), np.uint8)
for i in range(height):
    for j in range(wdith):
        grayPIxel = gray[i, j]
        dst[i, j] = 255-grayPIxel  # 255-当前灰度值
cv2.imshow('dst', dst)
cv2.waitKey(0)

# sz照相机的底板效果
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# height = img.shape[0]
# wdith = img.shape[1]
# # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# dst = np.zeros((height, wdith, 3), np.uint8)
# for i in range(height):
#     for j in range(wdith):
#         b, g, r = img[i, j]
#         dst[i, j] = (255-b, 255-g, 255-r)  # 255当前灰度值
# cv2.imshow('dst', dst)
# cv2.waitKey(0)