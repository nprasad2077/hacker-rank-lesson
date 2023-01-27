import math
import os
import random
import re
import sys

arr = [-4, 3, -9, 0, 4, 1]

def plus_minus(arr):
    positive = 0
    negative = 0
    zero = 0

    for i in arr:
        if i > 0:
            positive +=1
        if i < 0:
            negative +=1
        if i == 0:
            zero +=1

    positiveRatio = positive/len(arr)
    negativeRatio = negative/len(arr)
    zeroRatio = zero/len(arr)

    print("{:.6f}".format(positiveRatio))
    print("{:.6f}".format(negativeRatio))
    print("{:.6f}".format(zeroRatio))




plus_minus(arr)