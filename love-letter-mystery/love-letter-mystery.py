#!/bin/python3

import math
import os
import random
import re
import sys

def theLoveLetterMystery(s):
    return sum(abs(ord(s[x]) - ord(s[len(s) - x - 1])) for x in range(len(s)//2))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
