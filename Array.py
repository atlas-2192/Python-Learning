import random
#list sample

Matrix = [[0 for x in xrange(1)] for x in xrange(1)] 
print Matrix[0][0]

'''
Matrix = [[0 for x in xrange(5)] for x in xrange(5)] 
print len(Matrix)
Matrix[0][0] = 1
Matrix[3][4] = 3
print "value is ",len(Matrix)-1, len(Matrix)-1, "=", Matrix[len(Matrix)-1][len(Matrix)-1]

val_array=[]
while True:
    x = random.randint(0,len(Matrix)-1)
    y = random.randint(0,len(Matrix)-1)
    if Matrix[x][y] == 0:
        print x,y,Matrix[x][y] 
        if random.randint(0,100) > 90:
            Matrix[x][y] = 4 
        else:
            Matrix[x][y] = 2
        print "go break"
        break
Matrix [0][0] = 1
str1 = ''.join(str(e) for e in Matrix)
print "finish", str1
'''
def print_array(ary):
    print "[", ','.join(str(e) for e in ary), "]"

def merge_array(line):
    ret_line = [0 for x in xrange(len(line))]
    ret_index = 0
    pre_v = -1
    for i in range ( 0, len(line) ):
        print ','.join(str(e) for e in ret_line), line[i], pre_v
        if line[i] != 0:
            if  line[i] == pre_v:
                ret_line[ret_index] = pre_v*2
                ret_index += 1
                pre_v=-1
            else:
                if pre_v == -1:                
                    pre_v = line[i]
                else:
                    ret_line[ret_index] = pre_v
                    ret_index += 1
                    pre_v = line[i]
    if pre_v != -1:
        ret_line[ret_index] = pre_v
    return ret_line
#print_array( merge_array([2, 0, 2, 4]))
#print_array( merge_array([8, 16, 16, 8]))
#print_array( merge_array([2, 2, 0, 8, 16, 32,32,0,2,4,4]))
#print_array( merge_array([0, 0, 2, 0]))

list1 = [4, 3, 2, 1]
list1 = list(reversed(list1)) # Need transfer back to list or it will get iterable not list
print print_array(list1), len(list1)

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
MAP = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 

print MAP[UP]           

if MAP[UP] == (1,0):
    print "ddd"