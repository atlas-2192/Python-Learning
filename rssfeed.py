# -*- coding: utf-8 -*-
import feedparser

'''
Force decode for string codec.
'''
def force_decode(string, codecs=['utf8', 'big5']):
    for i in codecs:
        try:
            return string.decode(i)
        except:
            pass

if __name__ == "__main__":
    rss_url = "http://www.evanlin.com/blog/?feed=rss2"
    print "Parsing rss data ....."
    feed = feedparser.parse(rss_url)

    if not feed:
        print "no result"
    else:
        print feed["url"], feed[ "version"]
        for feed_item in feed["items"]:
            print feed_item["title"]