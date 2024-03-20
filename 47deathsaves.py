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
	for j in range(5):
		roll = random.randint(1, 20)
		if roll < 10 and roll > 1:
			failure += 1
		elif roll >= 10 and roll < 20:
			success += 1
		elif roll == 1:
			failure += 2
		elif roll == 20:
			health += 1
				
		if failure >= 3:
			die += 1
			break
		elif success >= 3: 
			stable += 1
			break
		elif health == 1:
			revived += 1
			break

print("probability of die:", die / rounds)
print("probability of stabilize:", stable / rounds)
print("probability of revived:", revived / rounds)

