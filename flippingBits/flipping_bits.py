import math
import os
import random
import re
import sys


def flipping_bits(n):
    binary = f'{n:b}'
    binarySplit = [*binary]
    binaryGap = 32 - len(binarySplit)
    binaryConvert = []

    for i in range(binaryGap):
        binarySplit.insert(0, '0')

    for x in binarySplit:
        if x == '0':
            binaryConvert.append('1')
        if x == '1':
            binaryConvert.append('0')

    decimalConvert = int((''.join(binaryConvert)), 2)
    print(decimalConvert)
    return(decimalConvert)


    

flipping_bits(9)
flipping_bits(2147483647)
flipping_bits(1)
flipping_bits(0)

