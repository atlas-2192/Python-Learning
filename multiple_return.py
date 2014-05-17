'''
Return as class member with init value and name
'''
class ReturnValue(object):
  def __init__(y0, y1, y2):
     self.y0 = y0
     self.y1 = y1
     self.y2 = y2

def g(x):
  y0 = x + 1
  y1 = x * 3
  y2 = y0 ** y3
  return ReturnValue(y0, y1, y2)

'''
Return with key map
'''
def g(x):
  y0 = x + 1
  y1 = x * 3
  y2 = y0 ** y3
  return {'y0':y0, 'y1':y1 ,'y2':y2 }

'''
name tuple with naming tuple colume.
'''
import collections
point = collections.namedtuple('Point', ['x', 'y'])
p = point(1, y=2)
p.x, p.y
#1 2
p[0], p[1]
#1 2

'''
yield return values
'''
def f(x):
    y0 = x + 1
    yield y0
    yield x * 3
    yield y0 ** 4

a, b, c = f(5)
a
#6
b
#15
c
#1296
