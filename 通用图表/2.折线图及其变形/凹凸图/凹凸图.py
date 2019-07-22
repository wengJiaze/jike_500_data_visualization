# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 15:42:59 2019

@author: Jiaze Weng

TO:One is never too old to learn !
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("darkgrid")
sns.set_context("paper")
sns.set()

# 凹凸图就是用名词取代

df = pd.read_excel('auto_test.xlsx')
df=df.set_index('time')
fig=plt.figure(figsize=(10,6))
df.plot(kind='line',use_index=True,marker='o',ms=15,ylim = [0,3.5],xlim=[18077,18083])
plt.title('凹凸图')




