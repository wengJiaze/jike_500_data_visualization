# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:35:12 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 导入数据’
data = pd.read_excel('test_01.xlsx')
df_01 = data[['label','view_times','zan_num','cai_num']][data['platform_name']=='香山学院'].groupby('label').sum()

# 作图研究不同标签的阅读量占总体阅读量的百分比
df1 = df_01['view_times']

plt.axis('equal')  # 保证长宽相等
plt.pie(df1,
       explode = [0.1,0,0],
       labels = df1.index,
       colors=['c', 'g', 'grey'],
       autopct='%.2f%%',
       pctdistance=0.6,
       labeldistance = 1.2,
       shadow = True,
       startangle=0,
       radius=1.5,
       frame=False)
# 第一个参数：数据
# explode：指定每部分的偏移量,用于突出数据
# labels：标签
# colors：颜色
# autopct：饼图上的数据标签显示方式
# pctdistance：每个饼切片的中心和通过autopct生成的文本开始之间的比例
# labeldistance：被画饼标记的直径,默认值：1.1
# shadow：阴影
# startangle：开始角度
# radius：半径
# frame：图框
# counterclock：指定指针方向，顺时针或者逆时针
