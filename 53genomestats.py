#53genomestats.py by Zhiying He

import gzip
import sys
import math

gffpath = sys.argv[1]
feature = sys.argv[2]

#path = '../MCB185/data/A.thaliana.gff.gz'

def gff(gffpath, feature):
	lengths = []
	with gzip.open(gffpath, 'rt') as fp:
		for line in fp:
			if line[0] == '#': 
				continue
			words = line.split()
			if words[2] == feature:
				beg = int(words[3])
				end = int(words[4])
				lengths.append(end - beg + 1)
	return lengths

def minmax(vals):
	mini = vals[0]
	maxi = vals[0]
	for val in vals:
		if val < mini: mini = val
		if val > maxi: maxi = val
	return mini, maxi
	
def mean(vals):
	total = 0
	for val in vals: total += val
	return total / len(vals)
	
def stdv(vals):
	avg = mean(vals)
	variance = sum((x - avg) ** 2 for x in vals) / len(vals)
	return math.sqrt(variance)

def median(vals):
	vals.sort()
	n = len(vals)
	if n % 2 == 0:
		return (vals[n//2 - 1] + vals[n//2]) / 2
	else:
		return vals[n//2]

lengths = gff(gffpath, feature)
count = len(lengths)

mini, maxi = minmax(lengths)
avg = mean(lengths)
stdv = stdv(lengths)
median = median(lengths)

print("Count:", count)
print("Min:", mini)
print("Max:", maxi)
print("Mean:", avg)
print("Standard Deviation:", stdv)
print("Median:", median)
