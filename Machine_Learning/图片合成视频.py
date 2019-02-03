#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-3 下午12:13"

import cv2
img = cv2.imread('image1.jpg', 1)
size = (img.shape[1], img.shape[0])
print(size)
videoWrite = cv2.VideoWriter('2.mp4', -1, 5, size)  # １文件名称　２编码器　３帧率　４　视频大小　５大小
for i in range(1, 11):
    filename = 'image'+str(i)+'.jpg'
    img = cv2.imread(filename)
    videoWrite.write(img)  # data
print('end')