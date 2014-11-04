#coding:utf-8
import random

win_num = 0
draw_num = 0
lose_num = 0

print '锤子剪刀布\n1代表剪刀\n2锤子\n3布'

for x in xrange(1,10):
	r=int(raw_input('请输入你要出什么:'))
	com = random.randrange(1, 4)

	if com == r:
		print '电脑出剪刀，平局'
		draw_num = draw_num + 1

	elif com == 1 and r == 2:
		print '电脑出剪刀，你赢了'
		win_num = win_num + 1

	elif com == 1 and r == 3:
		print '电脑出剪刀，你输了'
		lose_num = lose_num + 1

	elif com == 2 and r == 1:
		print '电脑出锤子，你输了'
		lose_num = lose_num + 1

	elif com == 2 and r == 3:
		print '电脑出锤子，你赢了'
		win_num = win_num + 1

	elif com == 3 and r == 1:
		print '电脑出布，你赢了'
		win_num = win_num + 1

	elif com == 3 and r == 2:
		print '电脑出布，你输了'
		lose_num = lose_num + 1

	else:
		print '你输入的是什么玩意。。。'

print '\n统计  赢:' + str(win_num) + ' 输:' + str(lose_num) + ' 平:' + str(draw_num)





