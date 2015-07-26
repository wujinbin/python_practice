#-*- coding:utf-8 -*-

'计算完全数(它所有的真因子的和恰好等于它本身)'

def isperfect(num):
	count = num/2
	factor = []
	while count > 0:
		if num % count == 0:
			if count not in factor:
				factor.append(count)
			if num/count not in factor and count != 1:
				factor.append(num/count)
		count -= 1
	return True if num == sum(factor) else False
	
for num in range(1,10001):
	if isperfect(num):
		print num,'is perfect'