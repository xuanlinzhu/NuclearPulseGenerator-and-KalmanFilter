#-*-coding:utf-8-*-
#2021.7.21编写
#作者：紫渊 QQ：1757524710
#用于生成随机的核脉冲数
#输入一个核脉冲数的均值，产生当前均值下融合统计涨落规律的脉冲数
#可用于脉冲计数型核仪器的算法研究

from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.type_check import real
from NuclearPluse import NuclearPulseGenerator as NPG

class KF:
    def __init__(self):
        self.Q = 0.23
        self.R = 100
        self.P = 1 
        self.Kg = 1
        self.Out = 0.2

kf = KF()

def NPG_KalmanFilter(NowData):
        
    # 1 预测现在的值
    PreData = kf.Out
    kf.Q = (kf.Out/kf.R)**0.5
    # 2 预测系统协方差
    kf.P = kf.P + kf.Q

    # 3 计算卡尔曼增益
    kf.Kg = kf.P/(kf.P+kf.R)

    # 4 估计最优值
    kf.Out = PreData + kf.Kg*(NowData - PreData)

    # 5 更新系统协方差
    kf.P = (1-kf.Kg)*kf.P

    return kf.Out

#以下用于验证卡尔曼滤波效果
plt_X = []
Basic_Data = []
Filter_Data = []
Bias_Data = []
Real_Data = []
for i in range(0,10000):
    plt_X.append(i)
    real_num =1000-(i/10-500)**2/250+1
    Real_Data.append(real_num)
    num = NPG(real_num)
    Basic_Data.append(num)
    pre_num = NPG_KalmanFilter(num)
    Filter_Data.append(pre_num)
    Bias_Data.append(pre_num /real_num *100)
plt.scatter(plt_X,Basic_Data,c='g')
plt.plot(plt_X,Filter_Data,c='red')
plt.plot(plt_X,Bias_Data,c='y')
plt.plot(plt_X,Real_Data,c='b')
plt.axhline(90)
plt.axhline(110)
plt.show()

