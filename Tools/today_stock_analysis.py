#coding:utf-8

# 今日数据分析

import tushare as ts
import numpy as np

# 获取今天的数据
today_data = ts.get_today_all()

# 按换手率排序
# 降序 ascending=False
order_by_turnoverratio = today_data.sort_index(by='turnoverratio', ascending=False)

# 前10的索引
# index = np.arange(10) 
# top10 = order_by_turnoverratio.ix[index]

top10 = order_by_turnoverratio[0:9]
top10 = top10[['code', 'name', 'changepercent', 'open', 'trade', 'high', 'low', 'turnoverratio']]

print top10