# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:51:55 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import squarify

# 导入数据，制作矩阵属性图，研究四大物料，劳保，资产的各自地区的成本
data = pd.read_excel('cost_moni.xlsx')
df = data[['style','area','cost']].groupby(by=['style','area']).sum().reset_index()

# 画图
labels = df.apply(lambda x: str(x[0])+"\n("+str(x[1])+")",axis=1)
sizes = df['cost'].values.tolist()
plt.figure(figsize=(12,8))
squarify.plot(sizes=sizes,label=labels,alpha=0.8)
plt.title('成本矩阵树形图')
