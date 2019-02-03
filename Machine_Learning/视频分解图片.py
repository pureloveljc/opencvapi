#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-2 下午4:11"

# 1load 2info 3parse  4 imwrite
import cv2
cap = cv2.VideoCapture('/home/purelove/PycharmProjects/opencvprojects/Machine_Learning/road.mp4')
isOpen = cap.isOpened()  # 是否可以打开
print(isOpen)
# 帧率  每秒钟可以打开多少图片 一般人眼帧率>15
fps = cap.get(cv2.CAP_PROP_FPS)
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(fps, width, height)
i = 0
while (isOpen):
    if i ==10:
        break
    else:
        i += 1
    (flag, frame) = cap.read()  # 读取每一张ｆｌａｇ是否读取成功　　framｅ内容
    filename = 'image'+str(i)+'.jpg'
    print(filename)
    if flag == True:
        cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
print('end')