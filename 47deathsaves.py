#47deathsaves.py by Zhiying He

import random 

success = 0
failure = 0
health = 0

rounds = 10000

for i in range(rounds):
	roll = random.randint(1, 20)
	if roll < 10:
		failure += 1
	elif roll >= 10:
		success += 1
	elif roll == 1:
		failure += 2
	elif roll == 20:
		health += 1
		
	if failure >= 3:
		print("die")
	elif success >= 3:
		print("stable")
	elif health > 0:
		print("revived")

print("probability of stabilizes:", success / rounds)
print("probability of die:", failure / rounds)
print("probability of revives:", health / rounds)