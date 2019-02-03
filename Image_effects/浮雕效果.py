#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 下午12:34"
import cv2
import numpy as np
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
height = img.shape[0]
width = img.shape[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = np.zeros((height, width, 1), np.uint8)

for i in range(0, height):
    for j in range(width-1):
        graypo = int(gray[i, j])
        grayp1 = int(gray[i, j+1])
        newP = graypo-grayp1+150
        if newP > 255:
            newP = 255
        if newP < 0:
            newP = 0
        dst[i, j] = newP
cv2.imshow('dst', dst)
cv2.waitKey(0)