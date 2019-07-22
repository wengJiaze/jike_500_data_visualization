# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:38:16 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
'''
此节代码绘制散点图
'''
# matplotlib绘制散点图
# plt.scatter()散点图
# plt.scatter(x, y, s=20, c=None, marker='o', cmap=None, norm=None, vmin=None, vmax=None, 
# alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)

plt.figure(figsize=(8,6))
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y,marker='.',
           s = np.random.randn(1000)*100,
           cmap = 'Reds',
           c = y,
           alpha = 0.8,)
plt.grid()

# 散点矩阵图
# s：散点的大小
# c：散点的颜色
# vmin,vmax：亮度设置，标量
# cmap：colormap

# pd.scatter_matrix()散点矩阵
# pd.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, 
# grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwds)

df = pd.DataFrame(np.random.randn(100,4),columns = ['a','b','c','d'])
pd.scatter_matrix(df,figsize=(10,6),
                 marker = 'o',
                 diagonal='kde',
                 alpha = 0.5,
                 range_padding=0.1)
# diagonal：({‘hist’, ‘kde’})，必须且只能在{‘hist’, ‘kde’}中选择1个 → 每个指标的频率图
# range_padding：(float, 可选)，图像在x轴、y轴原点附近的留白(padding)，该值越大，留白距离越大，图像远离坐标原点



# seaborn绘制散点图
# 1、基本设置
# 绘制散点图

g = sns.FacetGrid(tips, col="time",  row="smoker")
# 创建一个绘图表格区域，设置好row、col并分组

g.map(plt.scatter, 
      "total_bill", "tip",    # share{x,y} → 设置x、y数据
      edgecolor="w", s = 40, linewidth = 1)   # 设置点大小，描边宽度及颜色
g.add_legend()
# 添加图例

# 分类

g = sns.FacetGrid(tips, col="time",  hue="smoker")
# 创建一个绘图表格区域，设置好col并分组，按hue分类

g.map(plt.scatter, 
      "total_bill", "tip",    # share{x,y} → 设置x、y数据
      edgecolor="w", s = 40, linewidth = 1)   # 设置点大小，描边宽度及颜色
g.add_legend()
# 添加图例


