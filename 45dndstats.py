# 45dndstats.py by Zhiying He

import random

limit = 100

#3D6: roll 3 six-sided dice
total3d6 = 0
for i in range(limit):
	score = 0
	for j in range(3):
		p = random.randint(1, 6)
		score += p
	total3d6 += score 
print(total3d6 / limit)

#3D6r1: roll 3 six-sided dice, but re-roll any 1s
total3d6r1 = 0
for i in range(limit):
	score = 0
	for j in range(3):
		p = random.randint(1, 6)
		if p == 1:
			p = random.randint(1, 6)
		score += p
	total3d6r1 += score  
print(total3d6r1 / limit)

#3D6x2: roll pairs of six-sided 3 times, taking the maximum each time
total3d6x2 = 0
for i in range(limit):
	score = 0
	for j in range(3):
		p1 = random.randint(1, 6)
		p2 = random.randint(1, 6)
		if p1 >= p2:
			score += p1
		else:
			score += p2
	total3d6x2 += score 
print(total3d6x2 / limit)

#4D6d1: roll 4 six-sided dice, dropping the lowest die roll
total4d6d1 = 0
for i in range(limit):
	score = 0
	p1 = random.randint(1, 6)
	p2 = random.randint(1, 6)
	p3 = random.randint(1, 6)
	p4 = random.randint(1, 6)
	
	if p1 >= p4 and p2 >= p4 and p3 >= p4:
		score += p1 + p2 + p3
	elif p1 >= p3 and p2 >= p3 and p4 >= p3:
		score += p1 + p2 + p4
	elif p1 >= p2 and p3 >= p2 and p4 >= p2:
		score += p1 + p3 + p4
	else:
		score += p2 + p3 + p4
	total4d6d1 += score 
print(total4d6d1 / limit)

