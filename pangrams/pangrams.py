import math, os , random, sys, re

s = 'The quick brown fox jumps over the lazy dog'
s2 = 'We promptly judged antique ivory buckles for the next prize'
s3 = 'not one'

def pangram(s):
    bank = []
    word = s.upper().split(" ")
    words = list((''.join(word)))
    pangram = True

    for i in range(26):
        bank.append(0)
    
    for i in words:
        position = ord(i) - 65
        bank[position] = bank[position] + 1

    for i in bank:
        if i == 0:
            pangram = False
    
    if pangram == True:
        return 'pangram'
    else:
        return 'not pangram'



    
    

    


pangram(s)
pangram(s2)
pangram(s3)
