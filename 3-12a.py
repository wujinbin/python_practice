#coding:utf-8

'用户选择创建文件或者读取文件，简单文件读写'

import os
ls = os.linesep

def readTextFile():
	fName = raw_input('input a file name:')
	fPath = 'D:\\program\Python\%s' % fName
	try:
		fobj = open(fPath, 'r')
	except Exception as e:
		print "***File open error:",e
	else:
		for eachLine in fobj:
			print eachLine,
		fobj.close()
		
def writeTextFile():
	while True:
		fName = raw_input('input a file name:')
		fPath = 'D:\\program\Python\%s' % fName
		if os.path.exists(fPath):
			print "ERROR:File exists,input another name!"
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
	
def main():
	while True:
		choose = raw_input('input "r" or "w" to read or write file:')
		if choose == "r":
			readTextFile()
			break
		elif choose == "w":
			writeTextFile()
			break
		else:
			print 'invalid input!\n'

if __name__ == '__main__':
    main()