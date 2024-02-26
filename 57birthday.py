#57birthday.py by Zhiying He

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def paradox(trials, days, people):
	duplicate = 0
	for i in range(trials):
		calendar = [0] * days
		for j in range(people):
			birthday = random.randint(0, 364)
			calendar[birthday] += 1
			if calendar[birthday] > 1:
				duplicate += 1
				break  
	probability = duplicate / trials
	return probability

probability = paradox(trials, days, people)
print(probability)
