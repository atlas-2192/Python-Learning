import os
import re
# filename variables
filename = 'data//test_regex.txt'
newfilename = 'result.txt'

# read the file
if os.path.exists(filename):
    data = open(filename,'r')
    bulkemails = data.read()
else:
    print "File not found."
    raise SystemExit

# regex to get phone
# (01)2345-6789 , (01)23456789
# 0123456789
# 0911-234-567

r = re.compile(r'(\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)')
results = r.findall(bulkemails)
emails = ""
for x in results:
    print str(x)+"\n"