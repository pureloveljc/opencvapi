#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 下午10:41"
import cv2
import numpy as np
newImageinfo = (500, 500, 3)
dst = np.zeros(newImageinfo, np.uint8)
# 1dst 2左上角 3 右下角 4 颜色 5 是否填充  -1是填充 >0的值  就是线条宽度
# 矩形
cv2.rectangle(dst, (50, 100), (200, 300), (0, 225, 0), 5)
# 圆形
cv2.circle(dst, (250, 250), (50), (0, 255, 0), -1)
# 椭圆
cv2.ellipse(dst, (256, 256), (150, 100), 0, 0, 180, (0, 255, 0), -1)
# 任意多边形
points = np.array([[150, 50], [140, 140], [200, 170], [250, 250], [150, 50]], dtype=np.int32)
points = points.reshape((-1, 1, 2))

print(points.shape)
cv2.polylines(dst, [points], 1, (255, 255, 255))


cv2.imshow('dst', dst)
cv2.waitKey(0)
