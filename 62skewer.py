#62skewer.py by Zhiying He

import sys
import gzip
import mcb185
import dogma

gfp = sys.argv[1]
windowsize = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(gfp):

	init = seq[:windowsize]
	gcount = init.count('G')
	ccount = init.count('C')

	for i in range(1, len(seq) - windowsize + 1):
		old = seq[i - 1]
		new = seq[i + windowsize - 1]

		if old == 'G':
			gcount -= 1
		elif old == 'C':
			ccount -= 1

		if new == 'G':
			gcount += 1
		elif new == 'C':
			ccount += 1

		gc_content = dogma.gc_comp(seq[i:i+windowsize])
		gc_skew = dogma.gc_skew(seq[i:i+windowsize])
	
		print(f'GC content = {gc_content:.3f}')
		print(f'GC skew = {gc_skew:.3f}')
 
