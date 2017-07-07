import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range(len(arr) - 1, -1, -1):
    print(str(arr[i]) + ' ', end="")
