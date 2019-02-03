#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 下午10:56"
import cv2
import numpy as np

img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.rectangle(img, (200, 100), (500, 400), (0, 255, 0), 3)
cv2.putText(img, 'this is flow123', (100, 300), font, 1, (200, 100, 255), 2, cv2.LINE_AA)
cv2.imshow('img1', img)

height = int(img.shape[0]*0.5)
width = int(img.shape[1]*0.5)
imResize = cv2.resize(img, (width, height))
for i in range(0, height):
    for j in range(0, width):
        img[i+200, j+300] = imResize[i, j]
cv2.waitKey(0)