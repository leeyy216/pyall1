__author__ = 'LYY'
# -*- coding:utf-8 -*-

import urllib
import http.cookiejar
import re
import os
import selenium
from selenium import webdriver
import time
import bs4
from bs4 import Beautifulsoup

#山东大学绩点运算
class SDU:

    def __init__(self):
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
        time.sleep(3)
        dri.find_element_by_name("userName").send_keys('13122648')
        time.sleep(3)
        dri.find_element_by_name("password").send_keys('LyyLee216')
        time.sleep(3)
        dri.find_element_by_name("submitButton").click()
        time.sleep(3)
        dri.find_element_by_linkname("项目报名").click()
        time.sleep(3)
        dri.find_element_by_linkname("2013级2016-2017学年春季毕业设计（论文）").click()

        '''
    #获取本学期成绩页面
    def getPage(self):
        request  = urllib.Request(
            url = self.loginUrl,
            data = self.postdata)
        result = self.opener.open(request)
        result = self.opener.open(self.gradeUrl)
        #打印登录内容
        print (result.read().decode('gbk'))
'''

sdu = SDU()
#sdu.getPage()
