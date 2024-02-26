#57birthday.py by Zhiying He

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])


def birthday(people, days):
	calendar = [0] * days
	for i in range(people):
		birthday = random.randint(0, 364) 
		calendar[birthday] += 1 
	return calendar

    
def check(calendar):
	calendar.sort()
	for i in range(len(calendar)):
		for j in range(i + 1, len(calendar)):
			if calendar[i] == calendar[j]:
				return True
	return False
      
def paradox(trials, days, people):
	duplicate = 0
	for j in range(trials):
		calendar = birthday(people, days)
		if check(calendar):
			duplicate += 1
	return duplicate / trials


probability = paradox(trials, days, people)
print(probability)
