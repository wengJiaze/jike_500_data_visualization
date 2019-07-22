# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 10:42:05 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""
'''
此节我们介绍bokeh，并且用bokeh绘制散点图
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
基本绘图空间
'''
from bokeh.plotting import figure,show,output_file
# 导入图表绘制、图标展示模块
# output_file → 非notebook中创建绘图空间

import os
os.chdir('C:/Users/')
# 创建工作目录

output_file("circle.html")
# notebook绘图命令，创建html文件
# 运行后会弹出html窗口

p = figure(plot_width=400, plot_height=400)   # 创建图表，设置宽度、高度
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="blue", alpha=0.5)
# 创建一个圆形散点图

show(p)
# 绘图

'''
创建图表工具 
'''

# figure()

df = pd.DataFrame(np.random.randn(100,2),columns = ['A','B'])
# 创建数据

p = figure(plot_width=600, plot_height=400,    # 图表宽度、高度
           tools = 'pan,wheel_zoom,box_zoom,save,reset,help',  # 设置工具栏，默认全部显示
           toolbar_location='above',     # 工具栏位置："above"，"below"，"left"，"right"
           x_axis_label = 'A', y_axis_label = 'B',    # X,Y轴label
           x_range = [-3,3], y_range = [-3,3],        # X,Y轴范围
           title="测试图表"                       # 设置图表title
          )
# figure创建图表，设置基本参数
# tool参考文档：https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html

p.title.text_color = "white"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.title.background_fill_color = "black"
# 设置标题：颜色、字体、风格、背景颜色

p.circle(df['A'], df['B'], size=20,  alpha=0.5)
show(p)
# 创建散点图
# 这里.circle()是figure的一个绘图方法

# 颜色设置
# ① 147个CSS颜色，参考网址：http://www.colors.commutercreative.com/grid/
# ② RGB颜色值，参考网址：https://coolors.co/87f1ff-c0f5fa-bd8b9c-af125a-582b11

p.outline_line_width = 7         # 边框线宽
p.outline_line_alpha = 0.3       # 边框线透明度
p.outline_line_color = "navy"    # 边框线颜色
# 设置图表边框

p.background_fill_color = "beige"    # 绘图空间背景颜色
p.background_fill_alpha = 0.5        # 绘图空间背景透明度
# 背景设置参数

p.border_fill_color = "whitesmoke"    # 外边界背景颜色
p.min_border_left = 80                # 外边界背景 - 左边宽度
p.min_border_right = 80               # 外边界背景 - 右边宽度
p.min_border_top = 10                 # 外边界背景 - 上宽度
p.min_border_bottom = 10              # 外边界背景 - 下宽度

p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"
# 设置x轴线：标签、线宽、轴线颜色

p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"
# 设置y轴线：标签、字体颜色、字体角度

p.axis.minor_tick_in = 5      # 刻度往绘图区域内延伸长度
p.axis.minor_tick_out = 3   # 刻度往绘图区域外延伸长度
# 设置刻度

p.xaxis.bounds = (2, 4)
# 设置轴线范围

p.xaxis.axis_label = "Lot Number"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 30
# 设置标签名称、字体颜色、偏移距离

p.yaxis.axis_label = "Bin Count"
p.yaxis.axis_label_text_font_style = "italic"
# 设置标签名称、字体
p.xgrid.grid_line_color = None
# 颜色设置，None时则不显示

p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]
# 设置透明度，虚线设置
# dash → 通过设置间隔来做虚线

p.xgrid.minor_grid_line_color = 'navy'
p.xgrid.minor_grid_line_alpha = 0.1
# minor_line → 设置次轴线

p.xgrid.grid_line_color = None
# 设置颜色为空

p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"
# 设置颜色填充，及透明度

#p.grid.bounds = (-1, 1)
# 设置填充边界

p.legend.location = "bottom_left"
# 设置图例位置："top_left"、"top_center"、"top_right" (the default)、"center_right"、"bottom_right"、"bottom_center"
# "bottom_left"、"center_left"、"center"

p.legend.orientation = "vertical"
# 设置图例排列方向："vertical" （默认）or "horizontal"

p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"  # 斜体
p.legend.label_text_color = "navy"
p.legend.label_text_font_size = '12pt'
# 设置图例：字体、风格、颜色、字体大小

p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.5
# 设置图例外边线：宽度、颜色、透明度

p.legend.background_fill_color = "gray"
p.legend.background_fill_alpha = 0.2
# 设置图例背景：颜色、透明度

'''
总结一下：
Line Properties → 线设置
Fill Properties → 填充设置
Text Properties → 字体设置

1、Line Properties → 线设置  outline_ grid_ minor_grid_
（1）line_color，设置颜色
（2）line_width，设置宽度
（3）line_alpha，设置透明度
（4）line_join，设置连接点样式：'miter' miter_join，'round' round_join，'bevel' bevel_join
（5）line_cap，设置线端口样式，'butt' butt_cap，'round' round_cap，'square' square_cap
（6）line_dash，设置线条样式，'solid'，'dashed'，'dotted'，'dotdash'，'dashdot'，或者整型数组方式（例如[6,4]）

2、Fill Properties → 填充设置 background_  border_ band_ 
（1）fill_color，设置填充颜色
（2）fill_alpha，设置填充透明度

3、Text Properties → 字体设置  title.  label_
（1）text_font，字体
（2）text_font_size，字体大小，单位为pt或者em（ '12pt', '1.5em'）
（3）text_font_style，字体风格，'normal' normal text，'italic' italic text，'bold' bold text
（4）text_color，字体颜色
（5）text_alpha，字体透明度
（6）text_align，字体水平方向位置，'left', 'right', 'center'
（7）text_baseline，字体垂直方向位置，'top'，'middle'，'bottom'，'alphabetic'，'hanging'

4、可见性
p.xaxis.visible = False
p.xgrid.visible = False
基本参数中都含有.visible参数，设置是否可见
'''