#-*- coding:utf-8 -*-

'计算器程序，接收命令行参数（未做异常处理）'

import sys
import os

num = len(sys.argv)
params = sys.argv
s = os.linesep

if params[1].strip().lower() == 'print':
	f = open('data', 'r')
	for eachline in f:
		print eachline,
else:
	n1 = int(params[1].strip())
	operator = params[2].strip()
	n2 = int(params[3].strip())
	
	if operator == '+':
		result = n1+n2
	elif operator == '-':
		result = n1-n2
	elif operator == '*':
		result = n1*n2
	else:
		result = n1/n2
	print result
	
	f = open('data', 'a' if os.path.isfile('data') else 'w')
	f.write('%d%s%d%s%d%s' % (n1, operator, n2, s, result, s))
	f.close()