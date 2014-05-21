class ObjectA:
    obj_name = 'null'
    def __init__(self, name='null'):
        self.obj_name = name
        print '__init__%s' % self.obj_name
    def __enter__(self):
        print '__enter__%s' % self.obj_name
        return self
    def __exit__(self, type, value, traceback):
        print '__exit__%s' % self.obj_name
    def __del__(self):
        print '__del__%s' % self.obj_name
    def __str__(self):
        return '(%s)' % self.obj_name
    #any function first parameter will be self
    def print_obj(self, text):
        print 'n', self.obj_name

if __name__ == "__main__":   
    if True:
        a =  ObjectA('obj1')
        c =  ObjectA('obj3')
        #print init (once for each a/c)
        print str(a)

        # More detail about with http://effbot.org/zone/python-with-statement.htm
        with ObjectA('sss') as f1:
        #enter
        #more detail about enter/exist
        #http://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
            print 'in with'
            print type(f1), f1
            f1.print_obj('qqq')
            print 'end of with'
        #exist
    print 'finish'
    #print del