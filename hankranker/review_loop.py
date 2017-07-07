n = int(input())
strs = ["" for x in range(n)]
# input
for i in range(0, n, 1):
    strs[i] = str(input())
# output
for i in range(0, n, 1):
    str = strs[i]
    s_pre = ''
    s_post = ''
    for j in range(0, len(str), 1):
        if j % 2 == 0:
            s_pre = s_pre + str[j]
        else:
            s_post = s_post + str[j]
    print(s_pre, s_post)
