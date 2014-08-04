#coding:utf-8

import sqlite3
import os


'''
读取SQLite数据生成SQL的脚本
'''

ws_db = sqlite3.connect("/Users/aaa/Desktop/wsclientdb.db")

#获取游标
cursor = ws_db.cursor()

rfid_record = cursor.execute("select * from rfid_record2") 

# print '获取到的配对记录数量：', len(rfid_record.fetchall())
# fetchall()方法只能用一次 T.T

rfid_record_list = []

for record in rfid_record.fetchall():
	sql_barcode = "select * from barcode where barcode='" + record[2] + "'"
	barcode_cursor = cursor.execute(sql_barcode) 
	barcode = barcode_cursor.fetchall()
	wid = barcode[0][10]

	sql_barcode_attribute = "select * from barcode_attribute where bid=" + str(wid)
	attribute_cursor = cursor.execute(sql_barcode_attribute)
	attribute_list = attribute_cursor.fetchall()
	for attribute in attribute_list:
		if cmp(attribute[2].encode('utf-8'), '部门') == 0:
			info = [record[1], attribute[3]]
			rfid_record_list.append(info)




print '获取到的配对记录数量：', len(rfid_record_list)


# 新建文件写入结果
new_path_filename = "/Users/aaa/Desktop/sql_branch9.txt"
f = open(new_path_filename, 'w')

sql_insert = "INSERT INTO branch (id, epc, branch) select NULL, '77777', '777777'"
f.write(sql_insert)

for record in rfid_record_list[3991:]:
	f.write(" union all select NULL, '" + record[0].encode('utf-8') + "', '" + record[1].encode('utf-8') + "'\n")

f.close()




















	





