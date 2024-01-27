import math
import os
import random
import re
import sys

def sum_of_digits(num):
    return sum(int(digit) for digit in str(num))

def best_divisor(n):
    best_div = 1
    max_sum_of_digits = 1

    for divisor in range(2, n + 1):
        if n % divisor == 0:
            current_sum_of_digits = sum_of_digits(divisor)
             
            if current_sum_of_digits > max_sum_of_digits:
                max_sum_of_digits = current_sum_of_digits
                best_div = divisor
           
            elif current_sum_of_digits == max_sum_of_digits and divisor < best_div:
                best_div = divisor

    return best_div
 
n = int(input())

 
result = best_divisor(n)
print(result)
