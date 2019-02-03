#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-2-1 下午10:32"
import cv2
import numpy as np
newImageinfo = (500, 500, 3)
dst = np.zeros(newImageinfo, np.uint8)
# 绘制线段1 dst 2 线段起始位置 3 结束位置 4 颜色
cv2.line(dst, (100, 100), (400, 400), (0, 0, 255))

cv2.line(dst, (100, 200), (400, 200), (0, 0, 255), 20)  # 20宽度

cv2.line(dst, (100, 200), (400, 300), (0, 255, 0), 20, cv2.LINE_AA)  # 20宽度

# 三角形
cv2.line(dst, (200, 158), (50, 250), (25, 100, 255))
cv2.line(dst, (50, 250), (150, 350), (25, 100, 255))
cv2.line(dst, (150, 350), (200, 158), (25, 100, 255))

cv2.imshow('dst', dst)
cv2.waitKey(0)