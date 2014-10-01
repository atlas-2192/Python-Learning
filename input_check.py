
def is_input_number(any_input):
    try:
       val = int(any_input)
       return True
    except ValueError:
       return False

def is_input_string(any_input): 
    '''
    Any input could be string, so this always be True
    '''
    try:
       val = str(any_input)
       return True
    except ValueError:
       return False

print is_input_number("222") #True
print is_input_number("22a") #False
print is_input_string(222)   #True
print is_input_string("22")   #True


