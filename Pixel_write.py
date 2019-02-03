#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 上午9:06"
import cv2
import numpy as np

# 像素写入
img = cv2.imread('1.jpeg', 1)
b, g, r = img[100, 100]  # cv2读取像素的时候已bgr形式读取
# print(img[100:201, 10:12])
dst = np.zeros((100, 1, 3), np.int8)

# 10 100 ->110 100
for i in range(1000):
    img[10+i, 10] = (255, 255, 0)

cv2.imshow('image', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)  #1000 ms(毫秒)