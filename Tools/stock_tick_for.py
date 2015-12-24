#coding:utf-8

import tushare as ts
import time

code = '600171'
date = '2015-12-24'

def get_tick_data_sort_time(code, date):
    df = ts.get_tick_data(code=code, date=date)
    return df.sort_index(by='time', ascending=True)

df_sort_data = get_tick_data_sort_time(code, date)

buy_amount = 0
sale_amount = 0
level_amount = 0

i = 0
while i < df_sort_data.shape[0]:
    tick_data = df_sort_data[i:i+1]
    tick_data = tick_data[['time', 'price', 'change', 'volume', 'amount', 'type']]

    tick_type = tick_data.type.values[0]       # 买卖类型
    amount = tick_data.amount.values[0]        # 成交金额
    price = tick_data.price.values[0]
    scale_str = "-" * divmod(amount, 50000)[0] # 柱状图
    if tick_type == '买盘':
        buy_amount += amount
        print "\033[1;31m%s %-5s %-8s %s\033[0m"%(tick_data.time.values[0], price, tick_type, scale_str)
    elif tick_type == '卖盘':
        sale_amount += amount
        print "\033[1;32m%s %-5s %-8s %s\033[0m"%(tick_data.time.values[0], price, tick_type, scale_str)
    else:
        level_amount += amount
        print "%s %-5s %-8s %s "%(tick_data.time.values[0], price, tick_type, scale_str)
    time.sleep(0.05)
    i += 1

print '----------------'
print '买入:', buy_amount, '元'
print '卖出:', sale_amount, '元'
print '中性:', level_amount, '元'
