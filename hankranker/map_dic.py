import sys

n = int(input().strip())

d = {}
# input
for i in range(0, n, 1):
    name, val = input().strip().split(' ')
    d[name] = int(val)

# query
ret = []
key = input()

j = 0
while key != "":
    key_s = str(key)
    ret_str = ''
    if key not in d:
        ret_str = 'Not found'
    else:
        ret_str = key_s + '=' + str(d.get(key_s))
    ret.append(ret_str)
    j = j + 1
    if j < n:
        try:
            key = input()
        except EOFError:
            break
    else:
        break

# print ret
for i in range(0, len(ret), 1):
    print(ret[i])
