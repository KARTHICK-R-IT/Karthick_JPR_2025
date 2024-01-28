import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    # Check if the length of the string is even
    if len(s) % 2 != 0:
        return -1

    # Split the string into two substrings
    mid = len(s) // 2
    s1 = s[:mid]
    s2 = s[mid:]

    # Count the frequency of characters in each substring
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Calculate the minimum number of changes needed
    changes = 0
    for i in range(26):
        changes += abs(count_s1[i] - count_s2[i])

    # Return the result
    return changes // 2

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for _ in range(q):
        s = input().strip()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
