#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

escape_dict={'\a':r'\a',
           '\b':r'\b',
           '\c':r'\c',
           '\f':r'\f',
           '\n':r'\n',
           '\r':r'\r',
           '\t':r'\t',
           '\v':r'\v',
           '\'':r'\'',
           '\"':r'\"',
           '\0':r'\0',
           '\1':r'\1',
           '\2':r'\2',
           '\3':r'\3',
           '\4':r'\4',
           '\5':r'\5',
           '\6':r'\6',
           '\7':r'\7',
           '\8':r'\8',
           '\9':r'\9'}

def raw(text):
    """Returns a raw string representation of text"""
    new_string=''
    for char in text:
        try: new_string+=escape_dict[char]
        except KeyError: new_string+=char
    return new_string

# regex.py filename regex
if __name__ == '__main__':
	#print 'Number of arguments:', len(sys.argv), 'arguments.'	
	#print 'Argument List:', str(sys.argv)

	# filename variables
	filenamme = ''
	regex_string = ''

	if len(sys.argv) == 1: #No other parameter.
		print 'No other argument.'
		print '-------------------------'
		print ' regex.py filename regex'
		print '-------------------------'

		filename = 'data//test_regex.txt'
		''' 
		regex to get phone
		    (01)2345-6789 , (01)23456789
		    0123456789
		    0911-234-567
		''' 
		
		''' 
		About raw string conversion
		regex_string = r'(\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)'
		print 'search r string is :', regex_string 
		#search r string is : (\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)
		regex_string = '(\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)'.encode('string-escape')
		print 'search string is :', regex_string
		#search string is : (\x08(((\\d{10})|([\\(]??0\\d{1}[\\)]??\\d{4}[\\-]??\\d{4})|(0\\d{3}[\\-]??\\d{3}[\\-]??\\d{3})))\x08)
		regex_string = raw('(\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)')
		print 'search string is :', regex_string
		# search string is : (\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)
		'''

		regex_string = raw('(\b(((\d{10})|([\(]??0\d{1}[\)]??\d{4}[\-]??\d{4})|(0\d{3}[\-]??\d{3}[\-]??\d{3})))\b)')
	# read the file
	else:
		filename = sys.argv[1]
		regex_string = str(sys.argv[2])

	if os.path.exists(filename):
	    data = open(filename,'r')
	    bulkemails = data.read()
	else:
	    print "File not found."
	    raise SystemExit

	r = re.compile(regex_string)
	results = r.findall(bulkemails)
	if len(results) > 0:
		print 'total result is:', str(len(results))
	for x in results:
	    print str(x[0])