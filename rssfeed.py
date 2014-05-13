# -*- coding: utf-8 -*-
import feedparser
from html2bbcode import parser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

'''
Force decode for string codec for input string (file or web)
'''
def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass
'''
Display encode for string display from utf8 to other (Mac UTF-8/ Windows CP950(big5))
if  sys.stdout.encoding == sys.getdefaultencoding():
    it means stdout could display string correctly
else:
    encode from utf8 to stdout.encoding set
'''
def display_encode(string):
    global is_std_default_equal_encoding
    try:
        is_std_default_equal_encoding
    except NameError:
        is_std_default_equal_encoding = 0
    #else:
        #print "sure, it was defined."

    if not is_std_default_equal_encoding:
        encoding_str1 = sys.stdout.encoding.upper()
        #print encoding_str1
        encoding_str2 = sys.getdefaultencoding().upper()
        #print encoding_str2
        is_std_default_equal_encoding = encoding_str1 == encoding_str2
        #print is_std_default_equal_encoding

        encode_id = sys.stdout.encoding
        #print "encode id is", encode_id
        if encode_id != None:
            #print 'using encoding'
            return string.encode(encode_id)
        else:
            return string
    else:
        #print 'skip encodoing'
        return string

if __name__ == "__main__":
    is_std_default_equal_encoding = 1
    rss_url1 = "http://www.evanlin.com/blog/?feed=rss2"
    rss_url2 = "http://www.mesotw.com/bbs/rss.php?fid=25&auth=XC%2BJZQY%2FS4nZo8sf%2F2iTWyoL%2FMb7Hk5bzA"
    rss_url3 = "http://blogs.myoops.org/lucifer.php?tempskin=_rss2"
    print "----------------Print system data---------------"
    print 'stdout encoding =', sys.stdout.encoding
    print 'default encoding =', sys.getdefaultencoding()
    print "-------------------------------------------------"
    print "Parsing rss data ....."
    feed = feedparser.parse(rss_url3)
    rss_items = []
    rss_descriptions = []
    if not feed:
        print "no result"
    else:
        #print feed["url"], feed[ "version"], feed.modified
        #feed.etag/modified only support modified wordpress other might not.
        for feed_item in feed["items"]:
            #print display_encode(feed_item["title"])
            rss_items.append(feed_item["title"])
            rss_descriptions.append(feed_item["description"])
            break;
            #print feed_item["description"]
        print len(rss_descriptions)
        print "-------------------------------------------------"
        print rss_descriptions[0]
        print "-------------------------------------------------"
        parser_html = parser.HTML2BBCode()
        print str(parser_html.feed(rss_descriptions[0]))