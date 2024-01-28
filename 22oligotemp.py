# 22oligotemp.py by Zhiying He

def oligotemp(A, C, G, T):
    if A + C + G + T <= 13:
        Tm = (A+T)*2 + (G+C)*4
    else:
        Tm = 64.9 + 41*(G+C - 16.4)/(A+T+G+C)
    return Tm
    
print(oligotemp(1, 2, 3, 4))
print(oligotemp(4, 5, 6, 7))
