import sys

n = int(input().strip())

d = {}
# input
for i in range(0, n, 1):
    name, val = input().strip().split(' ')
    d[name] = int(val)

# query
ret = []
key = str(input().strip())
j = 0
while True:
    ret_str = ''
    if key not in d:
        ret_str = 'Not found'
    else:
        ret_str = key + '=' + str(d.get(key))
    ret.append(ret_str)
    j = j + 1
    if j < n:
        key = str(input().strip())
    else:
        break

# print ret
for i in range(0, n, 1):
    print(ret[i])
