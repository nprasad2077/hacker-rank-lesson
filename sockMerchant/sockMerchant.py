import math, os, random, re, sys

n = 7
ar = [1, 2, 1, 2, 1, 3, 2]


def sockMerchant(n, ar):
    bank = {}
    pairs = 0
    for i in ar:
        bank.update({i: 0})
    for i in ar:
        bank[i] += 1

    for i in bank:
        pairs += math.floor(bank[i] / 2)

    print(pairs)
    return pairs


sockMerchant(n, ar)
