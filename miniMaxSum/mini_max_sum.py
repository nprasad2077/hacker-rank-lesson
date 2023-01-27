import math
import os
import random
import re
import sys

arr = [1, 2, 3, 5, 4]
arrTwo = [7, 69, 2, 221, 8974]

def miniMaxSum(arr):
    minSort = sorted(arr)
    maxSort = sorted(arr, reverse=True)
    maxSum = sum(maxSort[0:4:1])
    minSum = sum(minSort[0:4:1])

    print(minSum, maxSum)
 


miniMaxSum(arr)
miniMaxSum(arrTwo)






