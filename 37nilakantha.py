#37nilakantha.py by Zhiying He
#cooperate with Aman Panigrahi

total = 3
denom = 2

for i in range(1, 100000):
	if i % 2 == 0:
		total = total + (4 / (denom*(denom+1)*(denom+2)))
	else:
		total = total - (4 / (denom*(denom+1)*(denom+2)))
	denom = denom +2

print(total)
	
