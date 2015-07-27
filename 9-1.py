#-*- coding:utf-8 -*-

'文件过滤'

import os

linesep = os.linesep

filename = raw_input('please input file name:')
f = open(filename, 'w')
print 'current directory:', os.getcwd()

f.write('hello world!\n')
f.write('hello python!\n')
f.write('#hello world!\n')
f.write('#hello python!\n')
f.close()

f = open(filename, 'r')

print 'num of lines:', len(f.readlines())

for eachline in f:
	if eachline[0] != '#':
		print eachline,
