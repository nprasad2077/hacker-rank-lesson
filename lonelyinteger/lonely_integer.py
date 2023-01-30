import math
import os
import random
import re
import sys

a = [1, 2, 3, 4, 3, 2, 1]


def lonelyinteger(a):
    for i in a:
        counter = 0
        for j in a:
            if i == j:
                counter+=1
        if counter == 1:
            print(i)
            return(i)



lonelyinteger(a)

