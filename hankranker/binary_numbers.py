#!/bin/python3

import sys


def dec2bin(d):
    # dec -> bin
    b = bin(d)
    return b

n = int(input().strip())
bin_str = dec2bin(n)

biggest_strike = 0
strike = 0

for c in dec2bin(n):
    if c == "1":
        strike = strike + 1
    else:
        strike = 0
    if strike > biggest_strike:
        biggest_strike = strike

print(biggest_strike)
