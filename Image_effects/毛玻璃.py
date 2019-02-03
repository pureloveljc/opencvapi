#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 上午10:30"

import cv2
import numpy as np
import random
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)
height = img.shape[0]
wdith = img.shape[1]
dst = np.zeros((height, wdith, 3), np.uint8)
mm = 8
for m in range(height-mm):
    for n in range(wdith-mm):
        index = int(random.random()*8)
        b, g, r = img[m+index, n+index]
        dst[m, n] = b, g, r
cv2.imshow('dst', dst)
cv2.waitKey(0)