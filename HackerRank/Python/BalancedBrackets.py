#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    c = 0
    while (True):
        if s.find('()') != -1:
            s = s.split('()')
            s = ''.join(s)
        elif s.find('{}') != -1:
            s = s.split('{}')
            s = ''.join(s)
        elif s.find('[]') != -1:
            s = s.split('[]')
            s = ''.join(s)
        else:
            c = len(s)
            break

    if c == 0:
        return 'YES'

    else:
        return 'NO'


if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)
        print(result)