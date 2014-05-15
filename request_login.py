# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from requests import session

payload = {
    'action': 'login',
    'email': 'evanslin@gmail.com',
    'password': '1217'
}

with session() as c:
    c.post('http://tw.gigacircle.com/login.html?redir=publisher.html', data=payload)
    request = c.get('http://tw.gigacircle.com/login.html?redir=publisher.html')
    #print request.headers
    print request.text