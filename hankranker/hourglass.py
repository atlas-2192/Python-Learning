#!/bin/python3

import sys


def hourglass_cal(start_i, start_j, Ary):
    return Ary[start_i][start_j] + Ary[start_i][start_j + 1] + Ary[start_i][start_j + 2] + Ary[start_i + 1][start_j + 1] + Ary[start_i + 2][start_j] + Ary[start_i + 2][start_j + 1] + Ary[start_i + 2][start_j + 2]

arr = []
len_i = 0
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    len_i = len(arr_t)
    arr.append(arr_t)

max_sum = 0
for j in range(0, 4):
    for i in range(0, 4):
        hourglass_sum = hourglass_cal(i, j, arr)
        if abs(hourglass_sum) > abs(max_sum):
            max_sum = hourglass_sum

print(max_sum)
