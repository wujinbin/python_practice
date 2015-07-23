#-*- coding:utf-8 -*-

d = {'b':1, 'c':4, 'a':2, 'd':0 }

#将字典中的键按照字母顺序显示
for key in sorted(d):
	print key, d[key]

#按照值顺序显示
for t in sorted(d.iteritems(), key = lambda d:d[1], reverse = False):
	print t