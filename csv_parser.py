#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv  
import json
import chardet
from chardet.universaldetector import UniversalDetector 

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
        	print "pass"
			

def parse_cvs_file_write_json(csv_file_name, char_set):
	f = open(csvfilename, 'r')
	#for row in csv.reader(f):  
	#	detector.feed(row)
	#	if detector.done: 
	#		break;
	#output =[]
	out = json.dumps( [row for row in csv.reader(f) ], encoding=char_set) 
	#print "JSON parsed!"  
	jsonfilename = csvfilename.split('.')[0] + '.json'
	jsonf = open(jsonfilename, 'w')  
	jsonf.write(out) 
	f.close()  


#open big5 csv
#http://data.gov.tw/node/5962
print 'hotspotlist.csv'
csvfilename = 'hotspotlist.csv'
parse_cvs_file_write_json(csvfilename, 'big5')


#open utf8 csv
#http://data.gov.tw/node/6794
print 'car-utf.csv'
csvfilename = 'car-utf.csv'
parse_cvs_file_write_json(csvfilename, 'utf8')
