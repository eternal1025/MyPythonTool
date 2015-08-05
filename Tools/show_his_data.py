#coding:utf-8

########################
# 显示股票是的历史走势
########################

import tushare as ts
import matplotlib.pyplot as plt

# 股票代码
stock_code = '601985'

# 获取历史数据
his_data = ts.get_hist_data(stock_code)

# 提取收盘价格
his_data = his_data[['close']]

# 绘图
his_data.plot()

# 显示
plt.show()