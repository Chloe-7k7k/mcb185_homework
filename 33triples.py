#33triples.py by Zhiying He

import math 

for i in range(1, 100):
	for j in range(i+1, 100):
		p = math.sqrt(i**2 * j**2)
		if p % 1 == 0 and p < 100:
			print(i, j, p)