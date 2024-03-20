#64profinder.py by Zhiying He

import dogma
import gzip
import sys
import mcb185


infile = sys.argv[1]
minlength = int(sys.argv[2])
#outfile = sys.argv[3]

for defline, seq in mcb185.read_fasta(infile):
	prot = []
	for i in range(3):
		rna1 = dogma.transcribe(seq[i:])
		rna2 = dogma.transcribe(mcb185.anti_seq(seq[i:]))
		pro1 = dogma.translate(rna1)
		pro2 = dogma.translate(rna2)
		prot.append(pro1)
		prot.append(pro2)
		
	protnum = 0
	for aa in prot:
		aaseq = aa.split('*')
		for proseq in aaseq:
			start = proseq.find('M')
			if start >= 0 and len(proseq[start:]) >= minlength:
				protnum += 1
				print(f'>{defline}-prot-{protnum}')
				print(proseq[start:] + '*')
