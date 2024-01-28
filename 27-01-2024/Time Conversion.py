#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Parse the input time string using datetime
    time_obj = datetime.strptime(s,'%I:%M:%S%p')

    # Format the time object in 24-hour format
    result = time_obj.strftime('%H:%M:%S')

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
l
