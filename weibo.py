#!D:\Program Files\Python35
#/usr/bin/python
#-*-coding:utf8-*-
#filename:weibo.py

import selenium

from selenium import webdriver
import time
'''20161208
#获得一个火狐浏览器对象，会打开火狐
ff = webdriver.Firefox()
#会进入weibo.com
#ff.get('http://weibo.com/')
ff.get('http://weibo.com/')
#每步操作留3秒时间  
time.sleep(5)
#输入用户名(你的微博账号)
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[1]/div/input").send_keys('13524328545')
time.sleep(3)
#输入密码（你的微博密码）
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/input").send_keys('GuANleeLE216')
time.sleep(3)
#点击登录
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[6]/a").click()

#写微博
time.sleep(10)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys('test from selenium')
#发布
time.sleep(3)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()


ff=webdriver.Firefox()

ff.get('https://www.baidu.com/')
time.sleep(5)

#ff.find_element_by_xpath("").sendkeys('selenium')
ff.driver.findElement(By.id("kw")).sendkeys('selenium')
ff.driver.findElement(By.id("su")).click()
'''
#20161209
#20161219

import os
iedriver="C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
ff = webdriver.Ie(iedriver)
#Ie是类，首字母大写

#会进入weibo.com
ff.get('http://weibo.com/')

#每步操作留3秒时间  
time.sleep(3)

#输入用户名(你的微博账号)
#ff.find_element_by_id("loginname").send_keys('13524328545')
ff.find_element_by_name("username").send_keys('13524328545')
time.sleep(1)

#输入密码（你的微博密码）
#ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/input").send_keys('GuANleeLE216')
ff.find_element_by_name("password").send_keys('11111111')
time.sleep(2)

#点击账号登录
#ff.find_element_by_class_name("cur W_fb").click()
ff.find_element_by_xpath("//div[@id='pl_login_form']/x:div/x:div[1]/x:div/x:a[1]").click()

#ff.get_log
#点击登录
#ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[6]/a").click()
#ff.find_element_by_class_name("W_btn_a btn_32px").click()

'''
#写微博
time.sleep(10)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys('test from selenium')
#发布
time.sleep(3)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()



#20161212

import os
ffdriver="D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
os.environ["webdriver.firefox.driver"] = ffdriver
ff = webdriver.Firefox(ffdriver)
#Ie是类，首字母大写

#会进入weibo.com
ff.get('http://weibo.com/')



#每步操作留3秒时间  
time.sleep(5)
#输入用户名(你的微博账号)
ff.find_element_by_id("loginname").send_keys('13524328545')
time.sleep(3)


#输入密码（你的微博密码）
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[2]/div/input").send_keys('GuANleeLE216')
time.sleep(3)
#点击登录
ff.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div[2]/div/div[2]/div[3]/div[2]/div[6]/a").click()

#写微博
time.sleep(10)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[2]/textarea').send_keys('test from selenium')
#发布
time.sleep(3)
ff.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[3]/div[2]/div[1]/div[1]/div/div[3]/div[1]/a').click()
'''
