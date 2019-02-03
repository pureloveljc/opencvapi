#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 下午3:53"
import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
height = img.shape[0]
weight = img.shape[1]
target_height = int(height/2)
target_weight = int(weight/2)
model = np.zeros((target_height, target_weight, 3), dtype=np.uint8)  # 0-255
# print(model)
# x*(src 行/目标 行)
for i in range(target_height):
    for j in range(target_weight):
        new_x = int(i*(height/target_height))
        new_y = int(j*(weight/target_weight))
        model[i, j] = img[new_x, new_y]
cv2.imshow('image', model)
cv2.waitKey(0)
