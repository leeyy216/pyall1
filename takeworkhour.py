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

url = 'http://10.4.246.116:26800/WorkHoursSystem/'
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
        

with open ('platformtable.txt','a') as file:
	file.write()
'''