
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2, urllib
import os
import csv  
import json
import chardet
import requests
from chardet.universaldetector import UniversalDetector 

'''
Need reset system to utf8 encode way to if we want to decode big5 string
http://legacy.python.org/dev/peps/pep-0263/
'''
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
			
def parse_cvs_to_json(handle_f, output_file, char_set):
	change_index = 0
	jsonf = open(output_file, 'w')  
	rows = []
	for row in csv.reader(handle_f):
		if 1: #change_index not in (0,2):  uncomment to skip what you don't want.
			#print force_decode(row[1])
			rows.append(row)
		else:
			print "skip in " + str(change_index)
		change_index += 1
	out = json.dumps(rows, encoding=char_set)
	print out
	jsonf.write(out) 	
	handle_f.close()  

def parse_file(source_type, source_file, output_file, char_set):
	if source_type == 'csv':
		f = open(source_file, 'r')
		parse_cvs_to_json(f, output_file, char_set)

def parse_url(source_type, source_address, output_file, char_set):
	if source_type == 'csv':
		#Use request.get to deal with very long URL.
		f = requests.get(source_address)
		parse_cvs_to_json(f.iter_lines(), output_file, char_set)

def parse_csv_url(source_address, output_file, char_set):
	parse_url('csv', source_address, output_file, char_set)

def parse_csv_file(source_file, output_file, char_set):
	parse_file('csv', source_file, output_file, char_set)

'''
def get_url_file(url_address, out_file_name, char_set):
	f = urllib2.urlopen(url_address)
	out = json.dumps( [row for row in csv.reader(f) ], encoding=char_set) 
	#print "JSON parsed!"  
	jsonf = open(out_file_name, 'w')  
	jsonf.write(out) 
'''
if __name__ == "__main__":
	url_address = 'http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fwww.thb.gov.tw%2FTM%2FFiles%2FWebpage%2F201404%2F16_%25E5%2585%25A8%25E5%259C%258B%25E5%25A4%25A7%25E5%25AE%25A2%25E8%25BB%258A%25E7%25A6%2581%25E8%25A1%258C%25E8%25B7%25AF%25E6%25AE%25B5-utf.csv&type=CSV&nid=6794'
	parse_csv_url(url_address, 'url2.json', 'utf8')
	print 'work!'


''' Sample file from OpenData.gov
#open big5 csv
#http://data.gov.tw/node/5962
csvfilename = 'hotspotlist.csv'
parse_csv_file('hotspotlist.csv', 'test2.json', 'big5')
parse_csv_url('http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fitaiwan.gov.tw%2Ffunc%2Fhotspotlist.csv&type=CSV&nid=5962', 'url.json', 'big5')

#open utf8 csv
#http://data.gov.tw/node/6794
print 'car-utf.csv'
csvfilename = 'car-utf.csv'
parse_csv_file(csvfilename, 'test2.json', 'utf8')
url_address = 'http://data.gov.tw/iisi/logaccess?dataUrl=http%3A%2F%2Fwww.thb.gov.tw%2FTM%2FFiles%2FWebpage%2F201404%2F16_%25E5%2585%25A8%25E5%259C%258B%25E5%25A4%25A7%25E5%25AE%25A2%25E8%25BB%258A%25E7%25A6%2581%25E8%25A1%258C%25E8%25B7%25AF%25E6%25AE%25B5-utf.csv&type=CSV&nid=6794'
parse_csv_url(url_address, 'url2.json', 'utf8')
'''
