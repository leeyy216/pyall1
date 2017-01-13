
# -*- coding: utf-8 -*-
#filename: takeplatform.py
#20161221
'''
from bs4 import BeautifulSoup
import urllib


url='http://172.31.27.22:8088/hbaq/system/platform/showList.do?csrftoken=5A67C8AA2D3B4459965674DE85F9A32A'
soup = BeautifulSoup(urllib.request.urlopen(url),"html5lib")
#,"html5lib"
#使用BeautifulSoup解析这段代码,能够得到一个 BeautifulSoup 的对象

#print(soup)
#print(soup.prettify())
#.prettify():以标准缩进格式
s = soup.title

#print(s.encode('utf-8'))
#print(type(s))
print (s)


#20161222-23##################################################################
#输出登录界面的h5代码
import bs4
from bs4 import BeautifulSoup
import urllib.request
import selenium
import time
import http.cookiejar
import re

url = 'http://172.31.27.22:8088/hbaq/system/platform/showList.do?csrftoken=E3008A56DF5A4DF3AE17926CC8741F93'
cookies = http.cookiejar.CookieJar()
soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html5lib")
response = urllib.request.urlopen(url)
html = response.read()

print (html.decode('utf-8'))
'''
#20161223###########################################################################
import bs4
from bs4 import BeautifulSoup
import urllib.request
import selenium
import time
#import cookielib   ：cookielib为python2中的库
import http.cookiejar
import re

url = 'http://172.31.27.22:8088/hbaq/'
url = 'http://172.31.27.22:8088/hbaq/system/platform/showList.do?csrftoken=181F62D2C0D54CBF9E65F23F64D444D1'
cookies = http.cookiejar.CookieJar()
#postdata = urllib.urlencode({'username':'hb_admin' 'pwd':'xxxxxx'})
#opener = urllib.request.build_opener(urllib.HTTPCookieProcessor(cookies))
#opener = urllib.request.urlopen

soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html5lib")
response = urllib.request.urlopen(url)
html = response.read()

#request = urllib.Request(url)
#result = opener.open(url)
print (html.decode('utf-8'))
'''
#biaotou = soup.select('body th')
#print(biaotou)
#登录URL
        self.loginUrl = 'http://itsmp.shu.edu.cn/admin/login.htm'
        #本学期成绩URL
        #self.gradeUrl = 'http://jwxt.sdu.edu.cn:7890/pls/wwwbks/bkscjcx.curscopre'
        #self.cookies = http.cookiejar()
        #self.postdata = urllib.urlencode({
        #    'stuid':'13122648',
        #   'pwd':'LyyLee216'
        # })
        #构建opener
        #self.opener = urllib.build_opener(urllib.HTTPCookieProcessor(self.cookies))
        iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = iedriver
        dri = webdriver.Ie(iedriver)
        dri.get(self.loginUrl)

with open ('platformtable.txt','a') as file:
	file.write()
'''
