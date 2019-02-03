#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 上午11:04"

import cv2
import numpy as np


def ImageHist(image, type):
    color = (255, 255, 255)
    windowname = 'Gray'
    if type == 31:
        color = (255, 0, 0)
        windowname = 'B Hist'
    elif type == 32:
        color = (0, 255, 0)
        windowname = 'G Hist'
    elif type == 32:
        color = (0, 0, 255)
        windowname = 'R Hist'
    # 1 image 2 [0]
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minv, maxV, minL, maxL = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 257, 3], np.uint8)
    for h in range(256):
        intenNormal = int(hist[h] * 256 / maxV)
        cv2.line(histImg, (h, 256), (h, 256 - intenNormal), color)
    cv2.imshow(windowname, histImg)

    return histImg


img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
channels = cv2.split(img)  # RGB -R-G-B
for i in range(3):
    ImageHist(channels[i], 31 + i)
cv2.waitKey(0)
