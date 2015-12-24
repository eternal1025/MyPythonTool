import tushare as ts

df_sort_data = ts.get_hist_data('600171', start='2015-10-1')
# df_sort_data = df.sort_index(ascending=True)

new_path_filename = "data.csv"
f = open(new_path_filename, 'w')
f.write("Date,Open,High,Low,Close,Volume\n")

i = 0
while i < df_sort_data.shape[0]:
    day_data = df_sort_data[i:i+1]
    p_open = day_data.open.values[0]
    p_close = day_data.close.values[0]
    p_high = day_data.high.values[0]
    p_low = day_data.low.values[0]
    p_volume = day_data.volume.values[0]
    date = day_data.index.values[0]

    f.write(str(date)+","+str(p_open)+","+str(p_high)+","+str(p_low)+","+str(p_close)+","+str(p_volume) + "\n")
    i += 1

f.close()
