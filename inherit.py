
class first:
    def func1(self, input1):
        print 'func1',input1
    def func2(self, input2):
        print 'func1'

class second(first):
    def func3(self, new_input1):
        print 'func3'
        print new_input1


print "ssss"
a1 = first()
b1 = second()
b1.func1('222')
