#46savingthrows.py by Zhiying He

import random 

trial = 100000


for dc in range(5, 16, 5):
	n = 0
	a = 0
	d = 0
	for i in range(trial):
		r1 = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r1 >= dc:
			n += 1
		if r1 >= r2:
			if r1 >= dc:
				a += 1
			if r2 >= dc: 
				d += 1
		else: 
			if r1 >= dc:
				d += 1
			if r2 >= dc: 
				a += 1
	print(f'{dc}\t{n/trial:.3f}\t{a/trial:.3f}\t{d/trial:.3f}')