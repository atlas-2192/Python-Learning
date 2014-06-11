import random
#list sample
Matrix = [[0 for x in xrange(5)] for x in xrange(5)] 
print len(Matrix)
'''print "--"
for i in range(0, 5-1):
    for j in range(0, 5-1):
        Matrix.append(0)
'''
Matrix[0][0] = 1
Matrix[3][4] = 3
print "value is ",len(Matrix)-1, len(Matrix)-1, "=", Matrix[len(Matrix)-1][len(Matrix)-1]

val_array = []
print len(Matrix)
print "--"
while True:
    for i in range (0,4):
        val_array.append(random.randint(0,5))
        print val_array[i]
    if val_array[0] != val_array[2] or val_array[0] != val_array[2]:
        print val_array
        break

Matrix [0][0] = 1