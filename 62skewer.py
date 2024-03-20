#62skewer.py by Zhiying He

import sys
import gzip
import mcb185
import dogma

gfp = sys.argv[1]
windowsize = int(sys.argv[2])

with gzip.open(gfp, 'rt') as fp:
	genome = ''
	for line in fp:
		if line[0] != '>':
			genome += line.strip()

init = genome[:windowsize]
gcount = init.count('G')
ccount = init.count('C')

for i in range(1, len(genome) - windowsize + 1):
	old = genome[i - 1]
	new = genome[i + windowsize - 1]

	if old == 'G':
		gcount -= 1
	elif old == 'C':
		ccount -= 1

	if new == 'G':
		gcount += 1
	elif new == 'C':
		ccount += 1

	gc_content = dogma.gc_comp(genome[i:i+windowsize])
	gc_skew = dogma.gc_skew(genome[i:i+windowsize])
	
	print(f'Window {i}: GC content = {gc_content:.3f}, GC skew = {gc_skew:.3f}')
 
	