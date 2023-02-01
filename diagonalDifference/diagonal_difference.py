import os
import math
import random
import re
import sys

arr = [ [ 11, 2, 4 ], [ 4, 5, 6 ], [ 10, 8, -12 ] ]
arrTwo = [ [ 11, 2, 4, 2 ], [ 4, 5, 6, 1 ], [ 10, 8, -12, 2 ], [5, 7, 3, 1] ]
arrThree = [[-1, 1, -7, -8], [-10, -8, -5, -2], [0, 9, 7, -1], [4, 4, -2, 1]]

# print(arr[1][1])


def diagonalDifference(arr):
    primary = 0
    secondary = 0
    counter = 0

    for i in range(len(arr)):
        print(arr[i][i])
        primary+=arr[i][i]
    
    for i in reversed(range(len(arr))):
        print(arr[i][counter])
        secondary+=arr[i][counter]
        counter+=1

    print(abs(primary - secondary))
    return abs(primary - secondary)


diagonalDifference(arr)