#55colorname.py by Zhiying He

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(p - q)
	return d
    
def minimum(vals):
	mini = vals[0]
	for val in vals[1:]:
		if val < mini: mini = val 
	return mini 

colorlist = []
colordis = []
user = (R, G, B)
with open(colorfile, 'rt') as fp:
	for line in fp:
		words = line.split()
		numbers = words[2]
		numbers = numbers.split(',')
		red = int(numbers[0])
		green = int(numbers[1])
		blue = int(numbers[2])
		colors = (red, green, blue)
		d = dtc(user, colors)
		colorlist.append(words[0])
		colordis.append(d)
		
minid = minimum(colordis)
colorindex = colordis.index(minid)
print(colorlist[colorindex])
