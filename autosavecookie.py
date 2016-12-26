#20161226
#takeworkhour
import bs4
from bs4 import BeautifulSoup
import urllib.request
import selenium
from selenium import webdriver
import time
#import cookielib
import http.cookiejar
import re
import os

cer = re.compile('name=\"_xsrf\" value=\"(.*)\"', flags = 0)
strlist = cer.findall(data)

url = "http://202.120.121.228:8991/pds?func=load-login&calling_system=aleph&url=http://202.120.121.228:8991/F/NPNVA8DGSHUTRSFN4MXBMH2TTJKPMHRNIQ6849TMPN48Q7MY3C-17050?func=find-b"
postdata =urllib.parse.urlencode({  
"func":"login",
"calling_system":"aleph",  
"bor_id":"13122648",
"bor_verification":"LyyLee216",
"bor_library":"SHU50",
"institute":"SHU50"
}).encode('utf-8')

# header = {
# "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
# "Accept-Encoding":"utf-8",
# "Accept-Language":"zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
# "Connection":"keep-alive",
# "Host":"c.highpin.cn",
# "Referer":None#"http://c.highpin.cn/",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
# }
req = urllib.request.Request(url,postdata)
##print(urllib.request.urlopen(req).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
print(r.read().decode('utf-8'))


'''
url = 'http://202.120.121.228:8991/pds?func=load-login&calling_system=aleph&url=http://202.120.121.228:8991/F/BFDA3M32TSAHLU7C6BKA7KLSCIRLP5NDQMDVJB9QE7JX5LJQ25-02979?func=find-b'
#url = 'http://172.31.27.22:8088/hbaq/system/platform/showList.do?csrftoken=E3008A56DF5A4DF3AE17926CC8741F93'

cookies = http.cookiejar.CookieJar()

iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
dri = webdriver.Ie(iedriver)
dri.get(url)

dri.find_element_by_name('NAME').send_keys("liyy")
dri.find_element_by_name('PASSWORD').send_keys("a1234567")
dri.find_element_by_id('commit').click()

#dri.find_element_by_linkname('项目报名').click()

soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html5lib")
response = urllib.request.urlopen(url)
html = response.read()

#postdata = urllib.urlencode({'username':'hb_admin' 'pwd':'xxxxxx'})
#opener = urllib.request.build_opener(urllib.HTTPCookieProcessor(cookies))
#opener = urllib.request.urlopen
#request = urllib.Request(url)
#result = opener.open(url)
print (html.decode('utf-8'))



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
        

with open ('platformtable.txt','a') as file:
	file.write()
'''