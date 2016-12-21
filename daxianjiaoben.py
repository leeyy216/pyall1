#-*-coding:utf8-*-
import selenium
from selenium import webdriver
import os

#ffdriver = "D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
#os.environ["webdriver.firefox.driver"] = ffdriver
ff = webdriver.Firefox()

ff.get("http://baidu.com")
