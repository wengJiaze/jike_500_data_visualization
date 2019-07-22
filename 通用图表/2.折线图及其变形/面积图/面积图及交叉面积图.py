# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:05:25 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据
data = pd.read_excel('test_01.xlsx')
df_01 = data[['publish_tm','view_times','zan_num','cai_num']][data['platform_name']=='香山学院'].groupby('publish_tm').sum()

# 简单面积图
fig,axes = plt.subplots(2,1,figsize = (8,6))
df1 = df_01['zan_num']
df2 = df_01['cai_num']

df1.plot.area(color = 'green',alpha = 0.5,ax = axes[0])
df2.plot.area(color = 'blue',alpha = 0.5,ax = axes[1])


# 交叉面积图‘
fig,axes = plt.subplots(2,1,figsize = (8,6))

df3 = df_01[['zan_num','cai_num']]
df3.plot.area(stacked=False,colormap='Set2',alpha=0.5,ax=axes[0])

# 也可写成：plt.fill(x, y1, 'r',x, y2, 'g',alpha=0.5)

x=df3.index
y1 = df3['zan_num'] 
y2 = df3['cai_num']
axes[1].fill_between(x, y1, y2, color ='g',alpha=0.5,label='area')  
# 填充两个函数之间的区域，使用fill_between函数

for i in range(2):
    axes[i].legend()
    axes[i].grid()


