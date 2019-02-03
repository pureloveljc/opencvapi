#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 下午3:30"

import cv2
import numpy as np
# p = p*1+40
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# height = img.shape[0]
# width = img.shape[1]
# dst = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
#     for j in range(width):
#         b, g,r = img[i, j]
#         bb = int(b*1.3)+40
#         gg = int(g*1.2)+40
#         rr = int(r)+40
#         if bb > 255:
#             bb=  255
#         if gg>255:
#             gg = 255
#         if rr >255 :
#             rr = 255
#         dst[i, j] = bb, gg, r
#
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

# 磨皮美白 双边滤波
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Picture_beautification/damaged.jpg', 1)
height = img.shape[0]
width = img.shape[1]
dst = cv2.bilateralFilter(img, 15, 35, 35)
cv2.imshow('dst', dst)
cv2.waitKey(0)