#23hydropathy.py by Zhiying He

def hydrophobicity(aa):
    if aa == "A":
        kd = 1.8
    elif aa == "C":
        kd = 2.5
    elif aa == "D":
        kd = -3.5
    elif aa == "E":
        kd = -3.5
    elif aa == "F":
        kd = 2.8
    elif aa == "G":
        kd = -0.4
    elif aa == "H":
        kd = -3.2
    elif aa == "I":
        kd = 4.5
    elif aa == "K":
        kd = -3.9
    elif aa == "L":
        kd = 3.8
    elif aa == "M":
        kd = 1.9
    elif aa == "N":
        kd = -3.5
    elif aa == "P":
        kd = -1.6
    elif aa == "Q":
        kd = -3.5
    elif aa == "R":
        kd = -4.5
    elif aa == "S":
        kd = -0.8
    elif aa == "T":
        kd = -0.7
    elif aa == "V":
        kd = 4.2
    elif aa == "W":
        kd = -0.9
    elif aa == "Y":
        kd = -1.3
    else:
        kd = "Error: not an amino acid."
    return kd

print(hydrophobicity("A"))
print(hydrophobicity("R"))
print(hydrophobicity("B"))
