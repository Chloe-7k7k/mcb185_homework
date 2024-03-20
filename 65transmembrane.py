#65transmembrane.py by Zhiying He

import mcb185
import sys

def kyte_doolittle(sequence):
	hydropathy_score = 0
	for aa in sequence:
		if aa == 'A':
			hydropathy_score += 1.8
		elif aa == 'R':
			hydropathy_score += -4.5
		elif aa == 'N':
			hydropathy_score += -3.5
		elif aa == 'D':
			hydropathy_score += -3.5
		elif aa == 'C':
			hydropathy_score += 2.5
		elif aa == 'Q':
			hydropathy_score += -3.5
		elif aa == 'E':
			hydropathy_score += -3.5
		elif aa == 'G':
			hydropathy_score += -0.4
		elif aa == 'H':
			hydropathy_score += -3.2
		elif aa == 'I':
			hydropathy_score += 4.5
		elif aa == 'L':
			hydropathy_score += 3.8
		elif aa == 'K':
			hydropathy_score += -3.9
		elif aa == 'M':
			hydropathy_score += 1.9
		elif aa == 'F':
			hydropathy_score += 2.8
		elif aa == 'P':
			hydropathy_score += -1.6
		elif aa == 'S':
			hydropathy_score += -0.8
		elif aa == 'T':
			hydropathy_score += -0.7
		elif aa == 'W':
			hydropathy_score += -0.9
		elif aa == 'Y':
			hydropathy_score += -1.3
		elif aa == 'V':
			hydropathy_score += 4.2
	return hydropathy_score / len(sequence)

file = sys.argv[1]

def signalpeptide(sequence):
	signalpeptide = sequence[:30]
    
	for i in range(len(signalpeptide) - 8 + 1):
		totalkd = 0
		sequence = signalpeptide[i:i+8]
		totalkd = kyte_doolittle(sequence)
		if totalkd >= 2.5 and 'P' not in sequence:
			return True
	return False 

def transmembrane(sequence):
	transmembrane = sequence[30:]
   
	for i in range(len(transmembrane) - 11 + 1):
		totalkd = 0
		sequence = transmembrane[i:i+11]
		totalkd += kyte_doolittle(sequence)
		if totalkd >= 2.0 and 'P' not in sequence:
			return True
	return False

count = 0
for defline, seq in mcb185.read_fasta(file):

	if signalpeptide(seq) and transmembrane(seq):
		print(f'>{defline[:60]}')
		count += 1
print(count)
		

         