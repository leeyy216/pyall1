# -*- coding:utf-8 -*-
#2017-1-5

import gzip
import re
import http.cookiejar
import urllib.request
import urllib.parse
import selenium
import bs4
from bs4 import beautifulsoup

'''
课题名	        上海高中自主招生信息的获取与管理
限报人数	1
课题类别	应用研究
课题性质	设计
是否新课题	是
课题来源	自拟
所需知识	数据库设计
课题简介	(包括课题意义、主要内容、目的要求，主要技术指标)
本课题旨在为小升初择校和初中生在高中自招时提供数据，为家长和孩子们提供支持。
要求能从上海招考热线的自招公示名单中
抓取上海四大高中名校以及示范性高中的自招信息并进行解析放入数据库，
同时能提供各类查询和统计、数据导入和导出等功能。

'''

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
    pro = urllib.request.HTTPCookieProcessor(cj)
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
    'Host': 'www.zhihu.com',
    'Content-Type': 'text/plain',
    'Referer': 'http://itsmp.shu.edu.cn/admin/login.htm',
    'Content-Length': '118',
    'Cookie': 'JSESSIONID=61222BCF8148DC57F321FF02A577828A',
    'Connection': 'keep-alive'
}
 
url = r'http://www.021xueli.com/'
opener = getOpener(header)
op = opener.open(url)

data = op.read()
data = str(data,"utf-8")
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
        'formToken': 'hb8RADlIoxuvAi1qoJTx8XgqbDi4cKjY'
}
postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
#data = ungzip(data)
 
print(data.decode())

