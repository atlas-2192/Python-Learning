
def charger(x, y):
	x=2			#copy by value
	y[0]=3		#copy by address not value for list, set

X=1
l=[2,4]

charger(X,l)
print "x="+str(X)+" l="
print l

#parameter by name which can switch (y,x)
charger(y=l, x=X)
print "x="+str(X)+" l="
print l


#module parameter test (*args)
def intersect(*args):
	res = []
	for x in args[0]:
		for y in args[1]:
			print "x="+x
			print "y="+y
			if x not in y: break
		else:
			res.append(x)
	return res

s1= "sAM"
s2="JAMES", "AME", "TIM"
print intersect(s1, s2)

#more detail about *args  and **args (keyword argments)
def foo(*arg):
	for x in arg:
		print x

def foo2(**arg):
	for x in arg:
		print x,"=", arg[x]
print "----------------------"
foo(3,4,5,6,7,8)
'''
3
4
5
6
7
8
'''
print "----------------------"
foo2(x=3,z=4,a=5,b=6,c=7,y=8) 
'''
a = 5
c = 7
b = 6
y = 8
x = 3
z = 4
'''
