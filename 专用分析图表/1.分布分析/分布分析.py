# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:18:44 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



'''
说明，分布分析是对一组数值型数据进行的分布确认。
例如，我们工作中接触的明细数据，比如每个订单产生的数据（重量，体积），对这一数据分析可以预测未来日均大概需要的包装材料的需求是多少
（当然要结合其他的分析，分布是其他的基础）
或者每天某地区的能产生的派件收件量，通过分布分析可以分析未来的某一天大概的件量会是多少？
故所有的分布数据会采取模拟数据进行分析，主要学习图表的制作方法及参数
'''
#--------------------------------------------------------
'''
这里引入了新的模块是seaborn，是matplotlib的升级，可以更简便且更多的图表进行展示
'''
sns.set_style("darkgrid")
sns.set_context("paper")
sns.set()
# 设置风格、尺度
#--------------------------------------------------------
# 直方图与密度图（分布图）
rs = np.random.RandomState(10)  # 设定随机数种子
s = pd.Series(rs.randn(100) * 100)
sns.distplot(s,bins = 10,hist = True,kde = False,norm_hist=False,
            rug = True,vertical = False,
            color = 'y',label = 'distplot',axlabel = 'x')
plt.legend()
# bins → 箱数
# hist、ked → 是否显示箱/密度曲线
# norm_hist → 直方图是否按照密度来显示
# rug → 是否显示数据分布情况
# vertical → 是否水平显示
# color → 设置颜色
# label → 图例
# axlabel → x轴标注

# 不同样式设计
sns.distplot(s,rug = True, 
            rug_kws = {'color':'g'} ,   
            # 设置数据频率分布颜色
            kde_kws={"color": "k", "lw": 1, "label": "KDE",'linestyle':'--'},   
            # 设置密度曲线颜色，线宽，标注、线形
            hist_kws={"histtype": "step", "linewidth": 1,"alpha": 1, "color": "g"})  
            # 设置箱子的风格、线宽、透明度、颜色
            # 风格包括：'bar', 'barstacked', 'step', 'stepfilled'
            
'''
分布图包含众多形式，箱线图，小提琴图
'''
# 箱线图
#导入模拟数据
tips = sns.load_dataset("tips")
sns.boxplot(x='day',y='total_bill',data=tips)
# 更多参数引入
sns.boxplot(x="day", y="total_bill", data=tips,
            linewidth = 2,   # 线宽
            width = 0.8,     # 箱之间的间隔比例
            fliersize = 3,   # 异常点大小
            palette = 'hls', # 设置调色板
            whis = 1.5,      # 设置IQR 
            notch = True,    # 设置是否以中值做凹槽
            order = ['Thur','Fri','Sat','Sun'],  # 筛选类别
           )
# 小提琴图
sns.violinplot(x='day',y='total_bill',data=tips)
# 通过hue进行分组再分组
sns.violinplot(x='day',y='total_bill',hue='smoker',data=tips)

# 分组后组合的小提琴图
sns.violinplot(x='day',y='total_bill',hue='smoker',data=tips,split=True) # 注意split的参数

            
# 2、密度图 - kdeplot()
# 两个样本数据密度分布图
# 多个密度图

rs1 = np.random.RandomState(2)  
rs2 = np.random.RandomState(5)  
df1 = pd.DataFrame(rs1.randn(100,2)+2,columns = ['A','B'])
df2 = pd.DataFrame(rs2.randn(100,2)-2,columns = ['A','B'])
# 创建数据

sns.kdeplot(df1['A'],df1['B'],cmap = 'Greens',
            shade = True,shade_lowest=False)
sns.kdeplot(df2['A'],df2['B'],cmap = 'Blues',
            shade = True,shade_lowest=False)
# 创建图表

# 1、综合散点图 - jointplot()
# 散点图 + 分布图

rs = np.random.RandomState(2)  
df = pd.DataFrame(rs.randn(200,2),columns = ['A','B'])
# 创建数据

sns.jointplot(x=df['A'], y=df['B'],  # 设置xy轴，显示columns名称
              data=df,   # 设置数据
              color = 'k',   # 设置颜色
              s = 50, edgecolor="w",linewidth=1,  # 设置散点大小、边缘线颜色及宽度(只针对scatter）
              kind = 'scatter',   # 设置类型：“scatter”、“reg”、“resid”、“kde”、“hex”
              space = 0.2,  # 设置散点图和布局图的间距
              size = 8,   # 图表大小（自动调整为正方形）
              ratio = 5,  # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15, rug=True)  # 设置柱状图箱数，是否设置rug
              )  

# 散点图 + 分布图
# 六边形图

df = pd.DataFrame(rs.randn(500,2),columns = ['A','B'])
# 创建数据

with sns.axes_style("white"):
    sns.jointplot(x=df['A'], y=df['B'],data = df, kind="hex", color="k",
                 marginal_kws=dict(bins=20))