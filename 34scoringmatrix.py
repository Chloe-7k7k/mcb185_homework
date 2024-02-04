print('  A  C  G  T')

alph = 'ACGT'

for nt1 in alph:
	print(nt1, end = '')
	
	for nt2 in alph:
		if nt1 == nt2: print('+1', end=' ')
		else:          print('-1', end=' ')

	print(end='\n')