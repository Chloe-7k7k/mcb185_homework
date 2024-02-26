
alphabet = 'ACGT'

print('  ', '  '.join(alphabet))

for nt1 in alphabet:
	print(nt1, end = ' ')
	
	for nt2 in alphabet:
		if nt1 == nt2: print('+1', end=' ')
		else:          print('-1', end=' ')

	print(end='\n')