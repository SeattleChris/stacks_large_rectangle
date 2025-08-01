#!/bin/python3

import os

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(lots):
    size = len(lots)
    if size < 2:
        return lots[-1] if lots else 0
    small = min(lots)
    shorts = [idx for idx, val in enumerate(lots) if val == small]
    x = 1 if shorts[0] == 0 else 0
    ends = [x] + [i for i in shorts if x < i < size] + [size]
    good = [largestRectangle(lots[a:b]) for a, b in zip(ends, ends[1:])]
    return max(small * size, *good)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    h = list(map(int, input().rstrip().split()))
    result = largestRectangle(h)
    fptr.write(str(result) + '\n')
    fptr.close()
