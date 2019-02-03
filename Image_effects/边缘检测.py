#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 上午11:30"

# 基于灰度  2 高斯滤波 3 canny

import numpy as np
import cv2
import random

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 0)
height = img.shape[0]
width = img.shape[1]

imgG = cv2.GaussianBlur(img, (3, 3), 0)  # 高斯滤波
dst = cv2.Canny(imgG, 50, 50)  # 50 门限
cv2.imshow('dst', dst)
cv2.waitKey(0)
