#!/bin/python3

import sys


def birthdayCakeCandles(n, ar):
    ar.sort(reverse=True)
    count = 0
    highest = ar[0]
    for c in range(0, n):
        if ar[c] == highest:
            count = count + 1
    return count
    # Complete this function

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)
