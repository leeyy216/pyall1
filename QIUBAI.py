# -*- coding:utf-8 -*-
#2016-12-26
import urllib
import urllib.request

page = 1
url = 'http://www.qiushibaike.com/'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

request = urllib.request.Request(url,headers = headers)
response = urllib.request.urlopen(request)
print (response.read())
'''
except urllib.error.URLError as e:
    if hasattr(e,"code"):
        print (e.code)
    if hasattr(e,"reason"):
        print (e.reason)
'''
