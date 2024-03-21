#64profinder.py by Zhiying He

import dogma
import gzip
import sys
import mcb185


infile = sys.argv[1]
minlength = int(sys.argv[2])
protnum = 0

for defline, seq in mcb185.read_fasta(infile):
	for i in range(3):
		rna1 = dogma.transcribe(seq[i:])
		rna2 = dogma.transcribe(mcb185.anti_seq(seq[i:]))
		
		pro1 = dogma.translate(rna1)
		pro2 = dogma.translate(rna2)
		
		
		for prot in (pro1, pro2):
			proteins = prot.split('*')
			for protein in proteins:
				if len(protein) >= minlength and protein[0] == 'M':
					protnum += 1
					print(f'>{defline}-prot-{protnum}')
					print(protein)

