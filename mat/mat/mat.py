# -*- coding: gbk -*-
import matplotlib.pyplot as plt
import random
import pandas as pd
from pylab import mpl
import numpy as np
# ������ʾ��������
mpl.rcParams["font.sans-serif"] = ["SimHei"]
# ����������ʾ����
mpl.rcParams["axes.unicode_minus"] = False
x=range(60)
y_shanghai=[random.uniform(20,40) for i in x]
plt.figure(figsize=(20,8),dpi=100)
plt.plot(x,y_shanghai)
x_ticks_lable=["11��{}��".format(i) for i in x]
y_ticks =range(40)
plt.xticks(x[::5],x_ticks_lable[::5])
plt.yticks(y_ticks[::5])
plt.grid(True,linestyle="--",alpha=0.5)
plt.xlabel("ʱ��")
plt.ylabel("�¶�")
plt.title("����11��--12��ĳ�����¶ȱ仯ͼ", fontsize=20)
plt.savefig("test.png")
subjects = ["����", "��ѧ", "Ӣ��", "����", "����"]
score=np.random.randint(0,100,(10,5))
print()
stu=['ͬѧ'+ str(i) for i in range(score.shape[0])]
stu=np.array(stu)
print(stu.shape)
stu.T
print(stu.shape)
new=pd.DataFrame(score,columns=subjects,index=stu)
print(new)