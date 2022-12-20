#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    p = []
    n = []
    zero = []
    for i in arr:
        if i > 0:
            p.append(i)
        if i < 0:
            n.append(i)
        if i == 0:
            zero.append(i)
    print(round(len(p) / len(arr), ndigits=6))
    print(round(len(n) / len(arr), ndigits=6))
    print(round(len(zero) / len(arr), ndigits=6))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
