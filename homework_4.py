# number 1
import pandas as pd
import numpy as np
import time
import matplotlib.pylab as plt
from pylab import mpl
from datetime import datetime
from calculated import average

df = pd.read_csv("apple.csv")
value = df.values
# number 2
totalavr = 0
print('平均股价：')
avrvul = average.averaged(value)
print(avrvul)
time.sleep(1)
# number 3
# 数值各种操作
# 设置中文字体
mpl.rcParams['font.sans-serif'] = ['SimHei']
everavr = sum(np.transpose(value[:, 2:4])) / 2
open = np.transpose(value[:, 1])
close = np.transpose(value[:, 4])
x = np.linspace(1, value.shape[0], value.shape[0])
fig = plt.figure(figsize=(16, 8))
coloall = ['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black']
line1 = plt.plot(x, everavr, label="平均价格", color=coloall[1], linewidth=0.5)
line2 = plt.plot(x, open, label="开盘价", color=coloall[2], linewidth=0.5)
line3 = plt.plot(x, close, label="收盘价", color=coloall[0], linewidth=0.5)
plt.xlabel("时间/天")
plt.ylabel("价格/美元")
plt.title("股价走势图(关掉此图程序继续运行)")
plt.show()
# number 4
sum = 0
for i in range(value.shape[0]):
    if everavr[i] > avrvul:
        sum += 1
        print(value[i][0])
print('以上日期的股价高于平均价格，总计有', sum, '天')
sum1 = 0
time.sleep(1)
for i in range(value.shape[0]):
    if everavr[i] < avrvul:
        sum1 += 1
        print(value[i][0])
print('以上日期的股价低于平均价格，总计有', sum1, '天')
time.sleep(1)
# number 5
df = pd.read_csv("d:/apple.csv")
value = df.values
summ = 0
sum = 0
toweek = -1
for i in range(value.shape[0]):
    timeArray = time.strptime(value[i][0], "%Y/%m/%d")
    otherStyleTime = time.strftime("%Y%m%d", timeArray)
    week = datetime.strptime(otherStyleTime, "%Y%m%d").strftime("%W")
    if int(week) == 0 and timeArray.tm_mon == 1:
        week = 52
    else:
        yearr = timeArray.tm_year
    if int(week) == toweek or i == 0:
        summ = summ + everavr[i]
        sum += 1
    elif int(week) != toweek:
        if toweek == 52:
            print('第', yearr - 1, '年', '第', toweek, '周的平均股价是：', summ / (sum))
            sum = 0
            summ = everavr[i]
        else:
            print('第', yearr, '年', '第', toweek, '周的平均股价是：', summ / (sum + 1))
    toweek = int(week)
print('第', yearr, '年', '第', toweek, '周的平均股价是：', summ / (sum + 1))
