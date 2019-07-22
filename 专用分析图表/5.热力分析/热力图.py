# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:24:31 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
此节代码为热力图代码
'''

#1、热图 - heatmap()
# 简单示例

df = pd.DataFrame(np.random.rand(10,12))
# 创建数据 - 10*12图表

sns.heatmap(df,    # 加载数据
            vmin=0, vmax=1   # 设置图例最大最小值
            )

# 2、热图 - heatmap()
# 参数设置

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers") 
print(flights.head())
# 加载数据
           
sns.heatmap(flights,
            annot = True,      # 是否显示数值
            fmt = 'd',         # 格式化字符串
            linewidths = 0.2,  # 格子边线宽度
            #center = 100,      # 调色盘的色彩中心值，若没有指定，则以cmap为主
            #cmap = 'Reds',     # 设置调色盘
            cbar = True,       # 是否显示图例色带
            #cbar_kws={"orientation": "horizontal"},   # 是否横向显示图例色带
            #square = True,     # 是否正方形显示图表
           )

# 半边热图
sns.set(style="white")
# 设置风格

rs = np.random.RandomState(33)
d = pd.DataFrame(rs.normal(size=(100, 26)))
corr = d.corr()   # 求解相关性矩阵表格
# 创建数据

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# 设置一个“上三角形”蒙版

cmap = sns.diverging_palette(220, 10, as_cmap=True)
# 设置调色盘

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=0.2)
# 生成半边热图