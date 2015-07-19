#coding:utf-8

'用户选择创建文件或者读取文件，简单文件读写'

import os
ls = os.linesep

while True:
	choose = raw_input("input 'r' or 'w':")
	if choose == 'r':
		fPath = raw_input('input a file path:')
		try:
			fobj = open(fPath, 'r')
		except Exception as e:
			print "***File open error:",e
			print
		else:
			for eachLine in fobj:
				print eachLine,
			fobj.close()
			break
	elif choose == 'w':
		while True:
			fPath = raw_input('input a file path:')
			if os.path.exists(fPath):
				print "Error:File exists, try another name!\n"
			else:
				break
			   
		content = []
		print "\nEnter lines('.' to exit).\n"
		
		while True:
			line = raw_input('> ')
			if line == '.':
				break
			else:
				content.append(line)
				
		fobj = open(fPath, 'w')
		fobj.writelines(['%s%s' % (x, ls) for x in content])
		fobj.close()
		print 'Write done!'
		break
	else:
	    print "invalid input!\n"