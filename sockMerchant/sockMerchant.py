import math, os, random, re, sys

n = 7
ar = [1, 2, 1, 2, 1, 3,2]

def sockMerchant(n, ar):
    bank = {4: 10}
    pairs = 0
    for i in ar:
        bank.update({i: 0})
        print(bank)

    for i in ar:
        bank[i]+=1
    
    print(bank)

    for i in bank:
        print(bank[i]/2)
        pairs += math.floor(bank[i]/2)
    
    print(pairs)









sockMerchant(n, ar)

