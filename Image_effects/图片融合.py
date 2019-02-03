#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 上午11:19"

import cv2
import numpy as np
img0 = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
img1 = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/Image_transformation/4e4a20a4462309f71ead3c36780e0cf3d6cad6d0.jpg', 1)

height = img0.shape[0]
width = img0.shape[1]

roih = int(height/2)
roiw = int(width/2)
img0ROI = img0[0:roih, 0:roiw]
img1ROI = img1[0:roih, 0:roiw]

dst = np.zeros((roih, roiw, 3), np.uint8)
dst = cv2.addWeighted(img0ROI, 0.5, img1ROI, 0.5, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
