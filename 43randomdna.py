#43randomdna.py by Zhiying He

import random 

seq = 10

for i in range(seq):
	seq_length = random.randint(50, 60)
	print(f'seq #{i}')
	for i in range(seq_length):
		print(random.choice('ACGT'), end='')
	print()
