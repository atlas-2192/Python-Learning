#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv  

'''
Need reset system to utf8 encode way to if we want to decode big5 string
http://legacy.python.org/dev/peps/pep-0263/
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
Check if content is unicode or ordinary string.
Usually it should be ordinary string.
print isinstance('這是中文',unicode) -> false
print isinstance(u'這是中文',unicode) -> true
'''
def whatisthis(s):
    if isinstance(s, str):
        print "ordinary string"
    elif isinstance(s, unicode):
        print "unicode string"
    else:
        print "not a string"
'''
Force trance code for string codec.
'''
def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
        	#print str(i)
            return string.decode(i)
        except:
            pass

#open big5 csv
#http://data.gov.tw/node/5962
print 'hotspotlist.csv'
f = open('hotspotlist.csv', 'r')  
for row in csv.reader(f):  
    print force_decode(row[1])  
f.close()  

#open utf8 csv
#http://data.gov.tw/node/6794
print 'car-utf.csv'
f = open('car-utf.csv', 'r')  
for row in csv.reader(f):  
    print force_decode(row[1])  
f.close()  

