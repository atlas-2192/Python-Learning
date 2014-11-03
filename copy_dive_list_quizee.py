n = 1000
numbers = range(2,n)
result = []

while len(numbers) > 0:
    num = numbers.pop(0)

    result.append(num)
    for num2 in numbers:
        if num2 % num == 0:
            numbers.remove(num2)
            print 'remove:', num2           

print len(result)