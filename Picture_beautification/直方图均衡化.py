#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 上午11:19"
# 直方图均衡化 更加高亮

import cv2
import numpy as np

# 灰度图像均衡化  本质 统计每个像素灰度出现的概率
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('src', gray)
# dst = cv2.equalizeHist(gray)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)

# 彩色图像均衡化
# img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg', 1)
# cv2.imshow('src', img)
# b, g, r = cv2.split(img)
# bH = cv2.equalizeHist(b)
# gH = cv2.equalizeHist(g)
# rH = cv2.equalizeHist(r)
# result = cv2.merge((bH, gH, rH))
# cv2.imshow('dst', result)
# cv2.waitKey(0)


# YUV 图像均衡化
img = cv2.imread('/home/purelove/PycharmProjects/opencvprojects/1.jpeg',1)
imgYUV = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('src', img)
channelYUV = cv2.split(imgYUV)
channelYUV[0] = cv2.equalizeHist(channelYUV[0])
channels = cv2.merge(channelYUV)
result = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)
cv2.imshow('dst', result)
cv2.waitKey(0)