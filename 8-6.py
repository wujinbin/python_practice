#-*- coding:utf-8 -*-

'素因子分解'

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
	factors.sort()
	return factors

def isprime(num):
	count = num/2
	while count > 1:
		if num % count == 0:
			return False
			break
		count -= 1
	else:
		return True
		
def primeCal(num):
	primefactor = []
	if not isprime(num):
		while not isprime(num):
			count = num/2
			for factor in range(2,count+1):
				if num % factor == 0:
					primefactor.append(factor)
					num /= factor
					break
		primefactor.append(num)
	else:
		return 'is prime' 
	return primefactor

def main():
	for num in range(1,41):
		print num,':',primeCal(num)
	
if __name__ == '__main__':
	main()