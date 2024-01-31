#21quadratic.py by Zhiying He

import math

def quadratic(a, b, c):
	D = b**2 - 4*a*c
	if D >= 0:
		x1 = (-b + math.sqrt(D)) / (2*a)
		x2 = (-b - math.sqrt(D)) / (2*a)
		return x1, x2
	if D < 0 :
		return 'no real root', 'no real root'


print(quadratic(1, 3, 5))
print(quadratic(1, -2, 2))


