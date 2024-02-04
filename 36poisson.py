#36poisson.py by Zhiying He

import math 

def poisson(n, k):
	probability = (n ** k * math.e ** -n) / math.factorial(k)
	return probability
    
print(poisson(24, 2))
print(poisson(100, 3))
print(poisson(67, 9))