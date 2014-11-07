''''
PiPy http://www.tuicool.com/articles/IJFV3i
How to install: #pip install flickrapi
documentation http://stuvel.eu/media/flickrapi-docs/documentation/
Api documentation http://stuvel.eu/media/flickrapi-docs/apidoc/
'''
import flickrapi
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

api_key = '000'
api_secret = '000'


def upload_func(progress, done):
    if done:
        print "Done uploading"
    else:
        print "At %s%%" % progress


flickr = flickrapi.FlickrAPI(api_key, api_secret, cache=True)
  
(token, frob) = flickr.get_token_part_one(perms='write')
if not token: 
    raw_input("Press ENTER after you authorized this program")
print token

flickr.get_token_part_two((token, frob))

flickr = flickrapi.FlickrAPI(api_key, api_secret, token=token)

'''
try:
    photos = flickr.walk(text='girl', tag_mode='all',
        tags='girl',
        min_upload_date='2014-02-05',
        max_upload_date='2014-02-06',
        extras='owner_name,tags,url_q,url_m,url_o')
except Exception:
    print 'error'
    exit()
        
try:
    for photo in photos:
        print photo.get('id'), photo.get('title')
        print photo.get('url_m')
        print ""

except Exception,ex:
    print 'error'
    print Exception,':',ex
'''

flickr.upload(filename='test.jpg', callback=upload_func)
print "done"