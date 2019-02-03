#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 上午10:15"
import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)
height = img.shape[0]
wdith = img.shape[1]
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
for m in range(100, 500):
    for n in range(100, 200):
        if m % 10 == 0 and n % 10 == 0:
            for i in range(0, 10):
                for j in range(0, 10):
                    print(i+m)
                    print(j+n)
                    b, g, r = img[m, n]
                    img[i+m, j+n] = b, g, r

cv2.imshow('dst', img)
cv2.waitKey(0)
