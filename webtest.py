# -*- coding=utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox()
browser.implicitly_wait(5)
browser.get('http://172.31.27.56:8088/bwyd/system/login')

# 登录

# 输入用户名
username = browser.find_element_by_id('username')
username.clear()
username.send_keys('wskict')
# 输入密码
password = browser.find_element_by_id('password')
password.clear()
password.send_keys('123456')
# 点击登录
login = browser.find_element_by_xpath('/html/body/div[2]/span/form/input')
login.click()

# 点击菜单：信息管理
browser.find_element_by_xpath("//*[@id='side-menu']/li[6]/a/span").click()
# 点击菜单：港口管理
browser.find_element_by_xpath("//*[@id='side-menu']/li[6]/ul/li[1]/a").click()
# 点击请选择
a = browser.find_element_by_xpath("//*[@id='dtTable']/tbody/tr[1]/td[9]/div/button")
# a.click()
# 点击修改选项
b = browser.find_element_by_xpath(
    "/html/body/section/div[2]/div[2]/form/div[3]/div[2]/div/table/tbody/tr[1]/td[9]/div/ul/li/a"
)
# b.click()
actions = ActionChains(browser)
actions.click(a).click(b).perform()


# 移除图片
c = WebDriverWait(browser, 5).until(
    EC.visibility_of(
        browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div[2]/div/div/form/div[2]/div[8]/div/div[1]/button"
        )))
c.click()
