print('   A  C  G  T')


for nt1 in 'ACGT':
	print(nt1, end = ' ')
	
	for nt2 in 'ACGT':
		if nt1 == nt2: print('+1', end=' ')
		else:          print('-1', end=' ')

	print(end='\n')