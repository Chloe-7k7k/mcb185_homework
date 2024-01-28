#21quadratic.py by Zhiying He

import math

def quadratic(a, b, c):

    #calculate the solution
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2

x1, x2 = quadratic(5, 6, 1)
print(x1, x2)


