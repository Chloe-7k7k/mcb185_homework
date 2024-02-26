#56birthday.py by Zhiying He

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

def birthday(people, days):
    birthdays = []
    for i in range(people):
        birthday = random.randint(0, 364)
        birthdays.append(birthday)
    return birthdays

"""
def check(birthdays):
    n = len(birthdays)
    for i in range(n):
        for j in range(i+1, n):
            if birthdays[i] == birthdays[j]:
                return True
    return False
"""

def check(birthdays):
    birthdays.sort()
    for i in range(1, len(birthdays)):
        if birthdays[i] == birthdays[i - 1]:
            return True
    return False
      
    
def paradox(trials, days, people):
    duplicate = 0
    for j in range(trials):
        birthdays = birthday(people, days)
        if check(birthdays):
            duplicate += 1
    return duplicate / trials


probability = paradox(trials, days, people)
print(probability)
