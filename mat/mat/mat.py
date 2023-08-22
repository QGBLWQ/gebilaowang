# -*- coding: gbk -*-
import matplotlib.pyplot as plt
import random
import pandas as pd
from pylab import mpl
import numpy as np
# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False
x=range(60)
y_shanghai=[random.uniform(20,40) for i in x]
plt.figure(figsize=(20,8),dpi=100)
plt.plot(x,y_shanghai)
x_ticks_lable=["11点{}分".format(i) for i in x]
y_ticks =range(40)
plt.xticks(x[::5],x_ticks_lable[::5])
plt.yticks(y_ticks[::5])
plt.grid(True,linestyle="--",alpha=0.5)
plt.xlabel("时间")
plt.ylabel("温度")
plt.title("中午11点--12点某城市温度变化图", fontsize=20)
plt.savefig("test.png")
subjects = ["语文", "数学", "英语", "政治", "体育"]
score=np.random.randint(0,100,(10,5))
print()
stu=['同学'+ str(i) for i in range(score.shape[0])]
stu=np.array(stu)
print(stu.shape)
stu.T
print(stu.shape)
new=pd.DataFrame(score,columns=subjects,index=stu)
print(new)