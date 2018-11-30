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
au = soup.find('div',class_ = "question__author")
author = au.find_next('strong').string
biaoti = soup.find('a',href = urlplus).string
with open(r'.\test.txt','a') as test:
    test.write("===%s start===%s\ntitle:%s\nauthor:%s\n"%(sys.argv[0], datetime.now().strftime("%Y-%m-%d %H:%M:%S"), biaoti, author))
    
while ar:
content = ""
    if num == 0:

        #user = ar.find("a",class = "answer__info--author-name")
        #username = user.find("strong").string
        #article = user.find_parent("article")
        #content = ar.find_next("p").string
        ar_ques = ar.find('div', class_ = 'question fmt')
        content1 = ar_ques.find("p").string
        content2 = ar_ques.find("span",)data-clipboard-text
        while (content1 or content2):
            if content1:
                content = content + content1
            else:
                content = content + content2

        time = ar.find_next("a").string
        #with open(r'.\test.txt','a') as test:
        #    test.write("楼主： %s 在 %s: %s\n" % (username,time,content))
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

;D:\Program Files\Python27\Scripts\;D:\Program Files\Python27\
D:\Program Files\Python35\Scripts\;D:\Program Files\Python35\;%SystemRoot%\system32;%SystemRoot%;%SystemRoot%\System32\Wbem;%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\;D:\Program Files\TortoiseSVN\bin;%USERPROFILE%\.dnx\bin;C:\Program Files\Microsoft DNX\Dnvm\;C:\Program Files (x86)\Windows Kits\8.1\Windows Performance Toolkit\;C:\Program Files\Microsoft SQL Server\130\Tools\Binn\;C:\strawberry\c\bin;C:\strawberry\perl\bin;D:\Program Files (x86)\HP\LoadRunner\strawberry-perl\perl\bin;D:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\;D:\Program Files (x86)\Microsoft SQL Server\100\DTS\Binn\;D:\Program Files (x86)\Microsoft SQL Server\100\Tools\Binn\VSShell\Common7\IDE\;C:\Program Files (x86)\Microsoft Visual Studio 9.0\Common7\IDE\PrivateAssemblies\;C:\Program Files\Microsoft SQL Server\110\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\ManagementStudio\;C:\Program Files (x86)\Microsoft SQL Server\110\Tools\Binn\;C:\Program Files (x86)\Microsoft SQL Server\110\DTS\Binn\;D:\Program Files (x86)\Mozilla Firefox\