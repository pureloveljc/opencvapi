#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "purelove"
__date__ = "19-1-31 上午10:22"
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import datetime

start = datetime.datetime(2019, 1, 5)  # 获取数据的时间段-起始时间
end = datetime.date.today()  # 获取数据的时间段-结束时间
stock = web.DataReader("000725.SZ", "yahoo", start, end)  #
end_price = np.array(stock['Close']).reshape(-1, 1)
open_price = np.array(stock['Open']).reshape(-1, 1)
print(end_price.shape)
plt.figure()
for i in range(int(end_price.shape[0])):
    dateone = np.zeros([2])
    dateone[0] = i
    dateone[1] = i
    priceOne = np.zeros([2])
    priceOne[0] = open_price[i]
    priceOne[1] = end_price[i]
    if open_price[i] < end_price[i]:
        plt.plot(dateone, priceOne, 'r', lw=8)
    else:
        plt.plot(dateone, priceOne, 'g', lw=8)
plt.show()
