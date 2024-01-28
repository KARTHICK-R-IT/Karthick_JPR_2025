import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr.sort()
    total_sum = sum(arr)
    min_sum = total_sum - arr[-1]
    max_sum = total_sum - arr[0]
    print(min_sum, max_sum)


if _name_ == '_main_':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
