import bs4
from bs4 import BeautifulSoup
import urllib.request
import http.cookiejar
import time
import os
import sys
import datetime
from datetime import datetime

baseurl = 'https://segmentfault.com'
urlnum = '1010000007243773'

urlplus = '/q/' + urlnum

url = baseurl + urlplus

cookies = http.cookiejar.CookieJar()
soup = BeautifulSoup(urllib.request.urlopen(url).read(),"html5lib")
#print (soup.decode('utf-8'))

#user = soup.find_next(title = 'panda0')
#username = user.string
#article = user.find_parent("article")
#content = article.find_next("p").string
#time = article.find_next("a").string
#with open(r'.\test.txt','a') as test:
#    test.write("%s 在 %s 说： %s" % (username,time,content))
num = 0
ar = soup.find("article")
author = 
biaoti = ar.find('a',href = urlplus).string
with open(r'.\test.txt','a') as test:
    test.write("===%s start===%s\ntitle:%s\n"%(sys.argv[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), biaoti))
    
while ar:

    if num == 0:

        #user = ar.find("a",class = "answer__info--author-name")
        user = ar.find('div',class_ = "question__author")
        username = user.find("strong").string
        #article = user.find_parent("article")
        #content = ar.find_next("p").string
        content = ar.find("p").string
        time = ar.find_next("a").string
        with open(r'.\test.txt','a') as test:
            test.write("楼主： %s 在 %s: %s\n" % (username,time,content))
    else:

        user = ar.find('a',class_ = "answer__info--author-name")
        username = user.string
        content = ar.find("p").string
        time = ar.find_next("a").string
        with open(r'.\test.txt','a') as test:
            test.write("%d楼： %s 在 %s: %s\n" % (num,username,time,content))
    num = num+1
    ar = ar.find_next("article")
        
#print()

#response = urllib.request.urlopen(url)
#html = response.read()
#print (html.decode('utf-8'))


