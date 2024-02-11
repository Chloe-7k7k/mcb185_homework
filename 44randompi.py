# 44randompi.py by Zhiying He

import random 

inside = 0
total = 0

while True:
	x = random.random()
	y = random.random()
	distance = (x ** 2 + y ** 2) ** 0.5

	if distance < 1:
		inside += 1 
	total += 1
	pi = 4 * (inside / total)
	print(f"Iteration: {total}, Pi: {pi}")
        