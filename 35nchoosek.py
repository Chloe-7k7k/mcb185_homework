#35nchoosek.py by Zhiying He
#cooperate with Yutong Ji

import math 

def factorial(n):
	if n == 0 or n == 1:
		return 1
	fac = 1
	for i in range(1, n + 1):
		fac = fac * i
	return fac

def nchoosek(n, k):
	if k < 0 or k > n:
		return 0
	else:
		return factorial(n) // (factorial(k) * factorial(n - k))

print(nchoosek(20, 4))
print(nchoosek(100, 7))
print(nchoosek(25, 5))