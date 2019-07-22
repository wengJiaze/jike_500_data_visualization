# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 14:00:06 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""
# ----------------------------------------------------------当前为matplotlib方法
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''本案例为了比较资讯号为“香山学院”下所有的文章的阅读量
'''
# 导入数据
data = pd.read_excel('test_01.xlsx')
df = data[data['platform_name']=='香山学院']

# 绘单一柱状图
fig=plt.figure(figsize=(10,6),dpi=80)
plt.bar(df['article_name'],df['view_times'],facecolor = 'gray',edgecolor='white',alpha=0.8) 
#此为画单一图表
# facecolor为填充颜色,edgecolor为边框颜色，alpha为透明度（0-1）
'''如果使用的jupyter notebook打开代码的话，
前面需要加上魔法函数%matplotlib inline(在下面直接显示)，
%matplotlib notebook(弹出可交互的matplotlib窗口)，
%matplotlib qt5（则弹出可交互性的控制台),
网页嵌入的
或者用plt.show()'''

# 参数设置
plt.title('graph title') # 图名
plt.xlabel('X label') # X轴标签
plt.ylabel('Y label') # y轴标签
plt.legend('upper right') # 显示图例，分别有对应的位置,此为右上
plt.xlim([-1,19]) # X轴范围,可以用来排序显示前几
plt.xticks() # 显示X刻度
plt.ylim([0,160]) # Y轴范围
plt.yticks() # 显示Y刻度
plt.grid(True,linestyle='--',color='gray',linewidth='0.5',axis='both')
 # 设置网格线，其中linestyle,linwidth,color为图表的样式参数，通用（常见于设置折线图）
 
 #介绍子图
 #当想在一个模块中展示多个图表
 # 方法一
 fig,axes = plt.subplots(2,3,figsize=(10,4)) # 先创建一系列图表，同时给他们定义上位置
 ax1 = axes[0,1] # 前为行索引，后卫列索引，即第一行的第二个子图
 
 # 方法二，用数据作图是的layout参数
 

