import math, os, random, re, sys

K = 10
A = [2, 1, 3]
B = [7, 9, 8]

K2 = 5
A2 = [1,2,2,1]
B2 = [3, 3, 3, 4]

K3 = 94
A3 = [84, 2, 50, 51, 19, 58, 12, 90, 81, 68, 54, 73, 81, 31, 79, 85, 39, 2]
B3 = [53, 102, 40, 17, 33, 92, 18, 79, 66, 23, 84, 25, 38, 43, 27, 55, 8, 19]



def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    
    return 'YES'






print(twoArrays(K2, A2, B2))



