# -*- coding: utf-8 -*-
import urllib2, urllib
import json
import sys
reload(sys)
sys.setdefaultencoding("utf-8") 

try:
    from pyquery import PyQuery as pq
except ImportError:
    print "pip install pyquery"
    sys.exit(1)


def read_file(fn):
    f = open(fn, 'r')
    #print f
    data = f.read()
    #print data
    f.close()
    return data

def parse_marker(xml):
    result = {}
    for key in keys:
    	print "get key"
        result[key] = xml.get(key)
        print result[key] 
    return result

if __name__ == "__main__":
    #first test parse string
    d=pq('<?xml version="1.0" encoding="utf-8" ?><Tutorial ><Title>Cake PHP 4 - Saving and Validating Data</Title><Categories><Category>Tutorials</Category></Tutorial>')
    d('Title')#返回[<p>,<p>]
    print d('Title')#返回<p>test 1</p><p>test 2</p>
    print d('Title').html()#返回test 1

    #second test parse URL
    #d = pq(url='http://www.baidu.com/')
    #print d('body').html()
    
    print "--------"
    #third test parse URL
    url_address ='http://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapXML&typeId=B'
    #d2 = pq(url=url_address)
    #print d2('emap').html()
    #d2('Info').attr('groupTypeName').html() #返回http://hello.com

    from lxml import etree
    print "Getting content from URL"
    #file_content = urllib.urlopen(url_address).read()
    file_1 = 'data/D_lvr_land_A.XML'
    file_2 = 'data/test1.xml'
    file_content = read_file(file_2)
    parser = etree.XMLParser(recover=True)
    xml_root = etree.fromstring(file_content, parser)
    #print etree.tostring(xml)
    #print xml_root[0].tag
    for sales in xml_root:
        print "{"
        for child in xml_root[0]:
            print child.tag, ':' , child.text
        print "}"
        #print(child.text)
        #print(child.value)
        #d = dict(child.attrb)
        ##sorted(d.items())
    print "finish"