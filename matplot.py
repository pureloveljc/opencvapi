#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 上午10:07"
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = np.array([2, 12, 53, 14, 5, 6, 7, 8])
plt.plot(x, y, 'r')  # 折线图
plt.plot(x, y, 'r', lw=5)  #
plt.bar(x, y, 0.5, alpha=0.5, color='b')  #  bar柱状图 alpha透明度
plt.show()
