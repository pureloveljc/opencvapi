#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-30 下午10:17"
# 1 引入opencv 2 api 3

import cv2
# 图片展示
img = cv2.imread('1.jpeg', 1)  # 参数0 灰度  参数1 彩色
print(img.shape)
cv2.imshow('image', img)  # 窗体名称
# cv2.waitKey(0)

# 图片写入
img1 = cv2.imread('1.jpeg', 1)
cv2.imwrite('image1.jpg', img1)  # 写入图片名称

# 图片质量
img2 = cv2.imread('1.jpeg', 1)
cv2.imwrite('image2.jpg', img2, [cv2.IMWRITE_JPEG_QUALITY, 0])

# 图片质量
img3 = cv2.imread('1.jpeg', 1)
cv2.imwrite('image3.jpg', img3, [cv2.IMWRITE_JPEG_QUALITY, 100])  # 0-100 牺牲图片质量 压缩图片

img4 = cv2.imread('1.jpeg')
cv2.imwrite('image4.png', img4, [cv2.IMWRITE_PNG_COMPRESSION, 0])  # 0-9 不牺牲图片质量 压缩比低

#  像素
#  RGB
#  颜色深度 8bit 0-255  256**3   图像在计算机中以二进制存储
#  图片的宽高 像素点
#  1.14M = 720*547*3 *8bit /8 (Byte) = 1.14
#     1Byte=8bit
# 　　1KB=1024Byte(字节)=8*1024bit
# 　　1MB=1024KB
#  RGB alpha透明度
#  bgr b g