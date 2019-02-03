#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午10:01"
import cv2
import numpy as np
# 方法一
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 0)
# cv2.imshow('img', img)
# cv2.waitKey(0)

# 方法二
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('img', dst)
# cv2.waitKey(0)

# 还有两种方法 rgb gray = (r+b+g)/3
# 灰度 很重要  人脸识别 行人识别都是以灰度作为基础
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# height = img.shape[0]
# width = img.shape[1]
# dst = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
#     for j in range(width):
#         (b, g, r) = img[i, j]
# 单通道图, 俗称灰度图
#         gray = (int(b)+int(g)+int(r))/3
#         dst[i, j] = np.uint8(gray)
# cv2.imshow('img', dst)
# cv2.waitKey(0)

# 方法四 gray = r*0.299+g*0.587+b*0.1114
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# height = img.shape[0]
# width = img.shape[1]
# dst = np.zeros((height, width, 3), np.uint8)
# for i in range(height):
#     for j in range(width):
#         (b, g, r) = img[i, j]
#         # 单通道图, 俗称灰度图
#         # int防治溢出
#         gray = int(r)*0.299+int(g)*0.587+int(b)*0.1114
#         dst[i, j] = np.uint8(gray)
# cv2.imshow('img', dst)
# cv2.waitKey(0)

#  算法优化
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
height = img.shape[0]
width = img.shape[1]
dst = np.zeros((height, width, 3), np.uint8)
for i in range(height):
    for j in range(width):
        (b, g, r) = img[i, j]
        # 单通道图, 俗称灰度图
        # int防治溢出
        gray = (int(r)*1+int(g)*2+int(b)*1)/4
        dst[i, j] = np.uint8(gray)
cv2.imshow('img', dst)
cv2.waitKey(0)