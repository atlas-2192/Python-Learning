'''
It is a learning code about import and from import
All related discussion comes from https://www.facebook.com/groups/pythontw/permalink/10152866933913438/?stream_ref=2
'''

print "from math import min"
from  math import cos #Not suggest because it will become naming confuse.
print cos(4)
print dir()
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cos']

print "import math as muh"
import math as muh #Suggest. It will use different name
print muh.cos(2)
print dir()
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cos', 'muh']

import math
import os

print "import math" #normal case, not confuse and indicate nameing function.
print math.log10(5)
print math.sin(15)
print dir()
#['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'cos', 'math', 'muh', 'os']
