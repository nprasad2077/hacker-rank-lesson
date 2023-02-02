import math, os, random, re, sys


s5 = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d5 = 18
m5 = 7


def birthday(s, d, m):
    segment = m
    counter = 0

    for i in range(len(s)-(segment)+1):
        portion = s[i:i+segment]
        total = sum(portion)
        print(total)
        if (total==d): counter+=1
    
    print(counter)
    return(counter)




birthday(s5, d5, m5)