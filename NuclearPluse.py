#-*-coding:utf-8-*-
#2021.7.21编写
#作者：紫渊 QQ：1757524710
#用于生成随机的核脉冲数
#输入一个核脉冲数的均值，产生当前均值下融合统计涨落规律的脉冲数
#可用于脉冲计数型核仪器的算法研究

#导入使用的模块
import numpy as np
import random as rd
from datetime import datetime





def NuclearPulseGenerator(AvrValue):
    #获取当前时间做随机数的种子
    NowTime = datetime.now().strftime("%M%S%f")
    np.random.seed(int(NowTime))

    #定义返回的随机脉冲
    BackPulse = 0.0

    #由于脉冲数低于10cps时，应该满足泊松分布
    #脉冲数大于16cps时，应该满足高斯分布
    #cps只是指代单位时间，单位时间可以不是s
    if(AvrValue<=0):
        BackPulse = -1
    elif((AvrValue>0)and(AvrValue<10)):
        BackPulse = np.random.poisson(lam=AvrValue)
    elif(AvrValue>16):
        BackPulse = rd.gauss(AvrValue,AvrValue**0.5)
    else:
        BackPulse = np.random.poisson(lam=AvrValue)

    
    #返回脉冲值
    return BackPulse

count = []
#测试函数结果
for i in range(0,100):
    count.append(NuclearPulseGenerator(0.8))


print(np.average(count))