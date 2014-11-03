slow_w = 1000
fast_w = 1.0
year   = 1

def OneYear():
    global slow_w
    global fast_w
    slow_w *= 2
    slow_w *= 0.6
    fast_w *= 2
    fast_w *= 0.7
    
x = 1
while True:
    print 'year', str(x) , 'slow:', slow_w, 'fast:', fast_w
    OneYear()
    x += 1
    if fast_w > slow_w:
        break