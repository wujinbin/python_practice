#-*- coding:utf-8 -*-

'接收一个整型作为参数，返回它所有约数的列表，包括1和自身'

def getfactors(num):
	factors = []
	count = num/2
	while count > 1:
		if num % count == 0:
			if num/count not in factors:
				factors.append(num/count)
			elif count not in factors:
				factors.append(count)
		count -= 1
	if num == 1:
		factors.append(1)
	else:
		factors.append(1)
		factors.append(num)
	return factors
	
print getfactors(20)
print getfactors(2)
print getfactors(1)