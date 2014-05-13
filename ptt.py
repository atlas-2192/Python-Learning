# -*- coding: utf-8 -*-
import feedparser
from html2bbcode import parser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import requests 
try:
    from pyquery import PyQuery as pq
except ImportError:
    print "pip install pyquery"
    sys.exit(1)


resp = requests.get(url="http://www.ptt.cc/bbs/Gossiping/M.1398931654.A.9A5.html", cookies={"over18": "1"})
#print(resp.content)
#using pq to parsing html detail content.
d = pq(resp.content)
print d('body').html()
