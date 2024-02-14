#47deathsaves.py by Zhiying He

import random 


die = 0
stable = 0
revived = 0

rounds = 100000

for i in range(rounds):
	success = 0
	failure = 0
	health = 0
	for j in range(4):
		roll = random.randint(1, 20)
		if roll < 10 and roll > 1:
			failure += 1
			if failure >= 3:
				die += 1
		elif roll >= 10 and roll < 20:
			success += 1
			if success >= 3: 
				stable += 1
		elif roll == 1:
			failure += 2
			if failure >= 3:
				die += 1
		elif roll == 20:
			health += 1
			if health == 1:
				revived += 1



print("probability of die:", die / rounds)
print("probability of stabilize:", stable / rounds)
print("probability of revived:", revived / rounds)
