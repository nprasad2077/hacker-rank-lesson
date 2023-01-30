import math
import os
import random
import re
import sys

time = '07:05:45PM'
timeTwo = '02:05:20AM'
timeThree = '12:03:20AM'
timeFour = '10:05:15PM'
timeFive = '11:15:30AM'

def timeConversion(s):
    day = s[8:9]
    hours = s[0:2]
    minutes = s[3:5]
    seconds = s[6:8]
    time_return = ''
    
    if hours == '12':
        hours = '00'
        time_return = hours + ':' + minutes + ':' + seconds

    if day == 'A':
        time_return = hours + ":" + minutes + ':' + seconds

    if day == 'P':
        hours = int(hours) + 12
        time_return = str(hours) + ':' + minutes + ':' + seconds
    
    print(time_return)
    return(time_return)




timeConversion(time)
timeConversion(timeTwo)
timeConversion(timeThree)
timeConversion(timeFour)
timeConversion(timeFive)
