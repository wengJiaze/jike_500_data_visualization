# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 23:15:06 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''本案例为了比较资讯号为“香山学院”下所有的文章的点赞点踩量
'''
# 导入数据
data = pd.read_excel('test_01.xlsx')
df = data[data['platform_name']=='香山学院'].set_index('article_name')

# 绘制条形图及堆叠条形图
fig,axes = plt.subplots(2,1,figsize = (10,10))
df_01 = df[['zan_num','cai_num']]
df_01['zan_num'].plot(kind='barh',ax=axes[0],grid=True,color='white')
df_01.plot.barh(grid=True,colormap='BuGn_r',stacked=True,ax=axes[1]) 
