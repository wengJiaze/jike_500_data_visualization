# -*- coding: utf-8 -*-
"""
Created on Thu Jul 18 22:38:29 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

# ----------------------------------------------------------当前为matplotlib方法
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''本案例为了比较资讯号为“香山学院”下所有的文章的点赞点踩量
'''
# 导入数据
data = pd.read_excel('test_01.xlsx')
df = data[data['platform_name']=='香山学院'].set_index('article_name')

# 多系列柱形图,与堆叠图
plt.style.use('fivethirtyeight') # style很重要，也很灵活简便
fig,axes = plt.subplots(2,1,figsize=(10,10))
df_01 = df[['zan_num','cai_num']]


df_01.plot(kind='bar',grid=True,colormap='Reds_r',ax=axes[0]) 
# 注意这里的另一种图形写法，用kind区分图表类型，且用colormap确定调色盘，ax为子图位置.colormap有哪些可以去查官网
df_01.plot(kind='bar',grid=True,colormap='Blues_r',ax=axes[1],stacked=True)
# 此为堆叠柱形图

