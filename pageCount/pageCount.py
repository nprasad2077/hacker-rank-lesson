import math, os, random, re, sys

n = 5
p = 3
n2 = 6
p2 = 2


def pageCount(n, p):
    back = n
    turn = p
    even = True
    if p%2!=0:
        even= False
        turn = turn -1
    if n%2 == 0:
        back = back + 1

    frontCount = int(turn/2)
    backCount = math.floor((back - p)/2)

    print(frontCount, backCount)

    if frontCount < backCount:
        print(frontCount)
        return(frontCount)
    else:
        print(backCount)
        return(backCount)


pageCount(n, p)
pageCount(10, 5)
pageCount(n2, p2)