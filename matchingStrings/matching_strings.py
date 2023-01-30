import math
import os
import random
import re
import sys

stringsOne = [ 'aba', 'baba', 'aba', 'xzxb' ]
queriesOne = [ 'aba', 'xzxb', 'ab' ]


def matching_strings(strings, queries):
    answer = []
    for i in queries:
        counter = 0
        for j in strings:
            if [i] == [j]:
                counter+=1
        answer.append(counter)
    print(answer)
    return(answer)


matching_strings(stringsOne, queriesOne)
    
        
