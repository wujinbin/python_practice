#-*- coding:utf-8 -*-

'判断一个数是否为素数'

def isprime(num):
	count = num/2
	while count > 1:
		if num % count == 0:
			return False
			break
		count -= 1
	else:
		return True
	
print isprime(2)
print isprime(7)
print isprime(20)