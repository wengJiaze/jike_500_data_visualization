# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:54:02 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
工具栏
'''
from bokeh.plotting import figure,show,output_file
# 导入图表绘制、图标展示模块
# output_file → 非notebook中创建绘图空间



# 工具栏 tools
# （1）设置位置

p = figure(plot_width=300, plot_height=300,
          toolbar_location="above")
# 工具栏位置："above"，"below"，"left"，"right"

p.circle(np.random.randn(100),np.random.randn(100))
show(p)

# 工具栏 tools
# （2）移动、放大缩小、存储、刷新

TOOLS = '''
        pan, xpan, ypan,             
        box_zoom,
        wheel_zoom, xwheel_zoom, ywheel_zoom,   
        zoom_in, xzoom_in, yzoom_in,
        zoom_out, xzoom_out, yzoom_out,
        save,reset
        '''

# （3）选择

TOOLS = '''
        box_select,lasso_select,
        reset
        '''
        
# （4）提示框、十字线  --------------这个非常有用

from bokeh.models import HoverTool
# 用于设置显示标签内容

df = pd.DataFrame({'A':np.random.randn(500)*100,
                  'B':np.random.randn(500)*100,
                  'type':np.random.choice(['pooh', 'rabbit', 'piglet', 'Christopher'],500),
                  'color':np.random.choice(['red', 'yellow', 'blue', 'green'],500)})
df.index.name = 'index'
source = ColumnDataSource(df)
print(df.head())
# 创建数据 → 包含四个标签

hover = HoverTool(tooltips=[
                            ("index", "$index"),
                            ("(x,y)", "($x, $y)"),
                            ("A", "@A"),
                            ("B", "@B"),
                            ("type", "@type"),
                            ("color", "@color"),
                        ])
# 设置标签显示内容
# $index：自动计算 → 数据index
# $x：自动计算 → 数据x值
# $y：自动计算 → 数据y值
# @A：显示ColumnDataSource中对应字段值

p1 = figure(plot_width=800, plot_height=400,toolbar_location="above",
            tools=[hover,'box_select,reset,wheel_zoom,pan,crosshair'])   # 注意这里书写方式
# 如果不设置标签，就只写hover，例如 tools='hover,box_select,reset,wheel_zoom,pan,crosshair'
p1.circle(x = 'A',y = 'B',source = source,size = 10,alpha = 0.3, color = 'color')
show(p1)

p2 = figure(plot_width=800, plot_height=400,toolbar_location="above",
           tools=[hover,'box_select,reset,wheel_zoom,pan'])
p2.vbar(x = 'index', width=1, top='A',source = source)
show(p2)
print(hover)