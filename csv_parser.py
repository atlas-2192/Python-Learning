#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv  
import json

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
csvfilename = 'hotspotlist.csv'
jsonfilename = csvfilename.split('.')[0] + '.json'

f = open(csvfilename, 'r')

loop_count = 0
output =[]
#主管機關	地區	熱點名稱	地址	緯度	經度
fieldnames = ("主管機關","地區","熱點名稱","地址", "緯度","經度")
for each in csv.reader(f):  
    #print force_decode(each[0])
    #print force_decode(each[1])
    row = {}
    row['主管機關'] = each[0]
    row['地區']  = each[1]
    row['熱點名稱']  = each[2]
    row['地址']   = each[3]
    output.append(row)
    print output 
    loop_count+=1
    #json.dump(row, jsonfile)
    #jsonfile.write('\n')
    if loop_count == 10:
    	break
out = json.dumps( [row for row in csv.reader(f) ], encoding='big5') 
print "JSON parsed!"  
jsonf = open(jsonfilename, 'w')  
jsonf.write(out) 
f.close()  

#open utf8 csv
#http://data.gov.tw/node/6794
print 'car-utf.csv'
f = open('car-utf.csv', 'r')  
loop_count = 0
for row in csv.reader(f):  
    print force_decode(row[1])  
    loop_count += 1
    if loop_count == 10:
    	break
f.close()  

