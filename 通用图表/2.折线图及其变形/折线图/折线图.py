# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:31:00 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''本案例为了研究资讯号为“香山学院”下所有的文章的点赞/点踩量的的趋势
'''
# 导入数据
data = pd.read_excel('test_01.xlsx')
df_01 = data[['publish_tm','view_times','zan_num','cai_num']][data['platform_name']=='香山学院'].groupby('publish_tm').sum()

# 画折线图
#plt.style.available  可查看可使用的style有哪些
plt.style.use('classic')
df_01[['zan_num','cai_num']].plot(
        kind='line',
        label = 'hehe',
        style = '-g.',
        color = 'red',
        alpha = 0.8,
        use_index = True,
        rot = 45,
        grid = True,
        ylim = [0,14],
        yticks = list(range(0,14,2)),
        figsize = (8,4),
        title = '香山学院所发文章的点赞/点踩数变化',
        subplots = False,
        legend = True)

#plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'x')  # 网格
plt.legend()
# Series.plot()：series的index为横坐标，value为纵坐标
# kind → line,bar,barh...（折线图，柱状图，柱状图-横...）
# label → 图例标签，Dataframe格式以列名为label
# style → 风格字符串，这里包括了linestyle（-），marker（.），color（g）
# color → 颜色，有color指定时候，以color颜色为准
# alpha → 透明度，0-1
# use_index → 将索引用为刻度标签，默认为True
# rot → 旋转刻度标签，0-360
# grid → 显示网格，一般直接用plt.grid
# xlim,ylim → x,y轴界限
# xticks,yticks → x,y轴刻度值
# figsize → 图像大小
# title → 图名
# subplots → 多系列是否变成子图
# legend → 是否显示图例，一般直接用plt.legend()
# 也可以 → plt.plot()