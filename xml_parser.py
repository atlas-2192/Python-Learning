# -*- coding: utf-8 -*-
"""
Convert an XML list of Tim Hortons restaurant locations to JSON
 
Usage: python parse.py sourcefile destfile
E.g.: python parse.py locations.xml locations.json
"""
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8") 

try:
    from pyquery import PyQuery as pq
except ImportError:
    print "pip install pyquery"
    sys.exit(1)
 
 
keys = ['鄉鎮市區', '總價元']
 
class objectJSONEncoder(json.JSONEncoder):
    """A specialized JSON encoder that can handle simple lxml objectify types
       >>> from lxml import objectify
       >>> obj = objectify.fromstring("<Book><price>1.50</price><author>W. Shakespeare</author></Book>")
       >>> objectJSONEncoder().encode(obj)
       '{"price": 1.5, "author": "W. Shakespeare"}'       
    """
    def default(self,o):
        if isinstance(o, lxml.objectify.IntElement):
        	print "sss"
        	return int(o)
        if isinstance(o, lxml.objectify.NumberElement) or isinstance(o, lxml.objectify.FloatElement):
            print "float"
            return float(o)
        if isinstance(o, lxml.objectify.ObjectifiedDataElement):
        	#print "saaaaaaa"
            return str(o)
        if hasattr(o, '__dict__'):
            #For objects with a __dict__, return the encoding of the __dict__
            print "dict"
            return o.__dict__
        return json.JSONEncoder.default(self, o)

def read_file(fn):
    f = open(fn)
    data = f.read()
    f.close()
    return data
 
 
def write_file(fn, stuff):
    f = open(fn, 'w')
    f.write(json.dumps(stuff, indent=4))
    f.close()
 
 
def parse_marker(xml):
    result = {}
    for key in keys:
    	print "get key"
        result[key] = xml.get(key)
        print result[key] 
    return result
 
 
def main(source, dest):
    print "read file"
    data = read_file(source)
    d = pq(data)
    a = d('marker')
    array = [parse_marker(x) for x in a]
    print "parse file"
    write_file(dest, array)
    print "write file"
 	
 
if __name__ == '__main__':
    try:
        source = "test1.xml"
        dest = "test1.json"
    except KeyError:
        print "Usage: python parse.py sourcefile destfile"
        print "E.g.: python parse.py locations.xml locations.json"
        sys.exit(1)
    main(source, dest)