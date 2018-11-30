# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import os
'''
iedriver="C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
ff = webdriver.Ie(iedriver)
webdriver.ff
'''
#ffdriver = "D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
#os.environ["webdriver.firefox.driver"] = ffdriver
ff = webdriver.Firefox()
ff.get("https://www.baidu.com")

ff.add_cookie({'name':'BAIDUID','value':'181E694A9DDCB85410C73B323E1AD3E4:FG=1'})
ff.add_cookie({'name':'BDUSS','value':'WVhUFBvTjRLY2NGQ2JzNjZXcU9TY05YUE1WV01uaFVEUTBjSll6anQwVy14V1ZaSVFBQUFBJCQAAAAAAAAAAAEAAABztkYCa2VhaWxpemk2MTUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL44Plm-OD5Zd'})

ff.refresh()

username = ff.find_element_by_class_name("user-name").text
print(username)

ff.quit()