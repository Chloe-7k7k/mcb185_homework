#25entropy.py by Zhiying He

import math

def entropy(a, c, g, t):
	if a < 0 or c < 0 or g < 0 or t < 0:
		return("Error: not a postive integer")
	else:
		nt = a + c + g + t
		p_a = a / nt
		p_c = c / nt
		p_g = g / nt
		p_t = t / nt
		if a != 0:
			S = 	(p_a*math.log2(p_a))
		if t != 0:
			S = S + (p_t*math.log2(p_t))
		if c != 0:
			S = S + (p_c*math.log2(p_c))
		if g != 0:
			S = S + (p_g*math.log2(p_g))
		return abs(S)
        
print(entropy(1, 2, 3, 4))
print(entropy(1, 3, 5, 7))


