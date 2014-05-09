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


if __name__ == "__main__":
    '''
    import xmltodict, json
    from lxml import etree

    file_1 = 'data/D_lvr_land_A.XML'
    file_2 = 'data/test1.xml'
    file_content = read_file(file_1)
    parser = etree.XMLParser(recover=True)
    xml_root = etree.fromstring(file_content, parser)
    content_string = etree.tostring(xml_root)
    print content_string
    print "--------"
    o = xmltodict.parse(content_string, encoding='big5')
    print json.dumps(o) # '{"e": {"a": ["text", "text"]}}'
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
    '''

    from lxml import etree
    print "Getting content from URL"
    file_1 = 'data/D_lvr_land_A.XML'
    file_2 = 'data/test1.xml'
    url_1  = 'http://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapXML&typeId=B'
    file_content = urllib.urlopen(url_1).read()
    #file_content = read_file(file_1)
    parser = etree.XMLParser(recover=True)
    xml_root = etree.fromstring(file_content, parser)
    #print etree.tostring(xml)
    #print xml_root[0].tag
    all_data = []
    map_d = {}
    
    ''' 'data/D_lvr_land_A.XML'
        <買賣>
            <鄉鎮市區>北區</鄉鎮市區>
            <交易標的>房地(土地+建物)</交易標的>
        </買賣>
    '''        
    for sales in xml_root:
        for child in sales:
            map_d[child.tag] = child.text
        all_data.append(map_d)
    ''' 
    <Info groupTypeName="工藝之家" 
        mainTypeName="工藝之家" 
     />
     '''
    for each_info in xml_root[0][0]:
        for attrs in each_info.iter('Info'):
            for key, value in attrs.attrib.iteritems():
                #print key, value
                map_d[key] = value
            all_data.append(map_d) 
    #print xml_root[0][0].tag
    print json.dumps(all_data) 
    print "finish"