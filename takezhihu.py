# -*- coding:utf-8 -*-
#2017-1-6

import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import selenium
from selenium import webdriver
import bs4
#from bs4 import beautifulsoup
import requests
#from requests import REQUEST
import time
import os

def ungzip(data):
    try:        # 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data
 
def getXSRF(data):
    cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
    strlist = cer.findall(data)
    return strlist[0]
 
def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookie8Processor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


header = {
    
    'Host': 'itsmp.shu.edu.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': 'text/html, application/xhtml+xml, application/xml; q = 0.9, */* ;q = 0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'text/plain',
    'Referer': 'http://itsmp.shu.edu.cn/admin/login.htm',
    'Content-Length': '118',
    'Cookie': 'JSESSIONID=61222BCF8148DC57F321FF02A577828A',
    'Connection': 'keep-alive'
}
 
url = r'http://itsmp.shu.edu.cn/admin/login.htm'
#'http://www.zhihu.com/'

#ff = webdriver.Firefox()
#driver.get(url)

opener = getOpener(header)
#op = opener.open(url)

#data = op.read()
#data = str(data,"utf-8")
#print(data)
#data = ungzip(data)     # 解压

#_xsrf = getXSRF(data.decode())
 
#url += '#signin'
userName = '13122648'
#'这里填你的知乎帐号'
password = 'LyyLee216'
#'这里填你的知乎密码'
postDict = {
       # '_xsrf':_xsrf,
        'userName': userName,
        'password': password,
       # 'formToken': 'hb8RADlIoxuvAi1qoJTx8XgqbDi4cKjY'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)

data = op.read()
#data = ungzip(data)
 
print(data.decode())

