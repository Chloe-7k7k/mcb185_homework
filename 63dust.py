#63dust.py by Zhiying He

import gzip
import sys
import math 
import mcb185

def entropy(a, c, g, t):
	if a < 0 or c < 0 or g < 0 or t < 0:
		return("Error: not a postive integer")
	else:
		nt = a + c + g + t
		entropy = 0
		p_a = a / nt
		p_c = c / nt
		p_g = g / nt
		p_t = t / nt
		if a != 0:
			entropy += (p_a*math.log2(p_a))
		if t != 0:
			entropy += (p_t*math.log2(p_t))
		if c != 0:
			entropy += (p_c*math.log2(p_c))
		if g != 0:
			entropy += (p_g*math.log2(p_g))
		return -entropy
		
path = sys.argv[1]
windowsize = int(sys.argv[2])
entropythreshold = float(sys.argv[3])


for defline, seq in mcb185.read_fasta(path):
	final = list(seq)

	for i in range(len(seq) - windowsize + 1):
		window = seq[i:i + windowsize]
		a = window.count('A')
		c = window.count('C')
		g = window.count('G')
		t = window.count('T')

		winentropy = entropy(a, c, g, t)
		if winentropy < entropythreshold:
			final[i:i + windowsize] = ['N'] * windowsize
		
	print(f'>{defline}', end='\n')
	complete = ''.join(final)		
	for i in range(0, len(complete), 60):
		print(complete[i:i+60])

