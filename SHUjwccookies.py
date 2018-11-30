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
#在测试用例中，执行完测试用例后，最后一步是判断测试结果是pass还是fail，自动化测试脚本里面一般把这种生成测试结果的方法称为断言（assert）。
#用unittest组件测试用例的时候，断言的方法还是很多的，下面介绍几种常用的断言方法：assertEqual、assertIn、assertTrue

#ffdriver = "D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
#os.environ["webdriver.firefox.driver"] = ffdriver
ff = webdriver.Firefox()
ff.get("https://www.baidu.com")

ff.add_cookie({'name':'BAIDUID','value':'181E694A9DDCB85410C73B323E1AD3E4:FG=1'})
ff.add_cookie({'name':'BDUSS','value':'WVhUFBvTjRLY2NGQ2JzNjZXcU9TY05YUE1WV01uaFVEUTBjSll6anQwVy14V1ZaSVFBQUFBJCQAAAAAAAAAAAEAAABztkYCa2VhaWxpemk2MTUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL44Plm-OD5Zd'})

ff.refresh()

# driver = self.driver
# driver.get(self.base_url)
ff.find_element_by_link_text(u"贴吧").click()
ff.find_element_by_id("wd1").send_keys("lovelive国服")
ff.find_element_by_link_text(u"进入贴吧").click()
# self.assertEqual(, self.close_alert_and_get_its_text())
ff.assertTextPresent(u"lovelive国服吧")
# #Select(driver.find_element_by_id("type")).select_by_visible_text(u"虚拟机")
# driver.find_element_by_xpath("//button[@type='button']").click()
# driver.find_element_by_link_text("fagag").click()
# driver.find_element_by_id("deviceName_v").clear()
# driver.find_element_by_id("deviceName_v").send_keys("lyytest5")
# driver.find_element_by_id("isPower1").click()
# driver.find_element_by_id("entityCode").clear()
# driver.find_element_by_id("entityCode").send_keys("123123")
# Select(driver.find_element_by_id("safetyDomain")).select_by_visible_text(u"网络交互域")
# driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
# driver.find_element_by_link_text("lyy tdtyku").click()
# driver.find_element_by_id("eniMacOne").clear()
# driver.find_element_by_id("eniMacOne").send_keys("11:11:11:11:11:11")
# driver.find_element_by_id("isOnline2").click()
# driver.find_element_by_id("isPower2").click()
# driver.find_element_by_id("isServer1").click()
# driver.find_element_by_id("onlineDate").send_keys("2016-12-01")
# driver.find_element_by_id("teturnTops").click()
# self.assertEqual(u"新增成功", self.close_alert_and_get_its_text())

username = ff.find_element_by_class_name("user-name").text
print("%s login success" % username)

ff.quit()

#执行测试的类
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget()
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    def testResize(self):
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))

#一个测试用例
class BaiduLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_hb_add(self):
        driver.add_cookie({'name':'BAIDUID','value':'181E694A9DDCB85410C73B323E1AD3E4:FG=1'})
        driver.add_cookie({'name':'BDUSS','value':'WVhUFBvTjRLY2NGQ2JzNjZXcU9TY05YUE1WV01uaFVEUTBjSll6anQwVy14V1ZaSVFBQUFBJCQAAAAAAAAAAAEAAABztkYCa2VhaWxpemk2MTUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL44Plm-OD5Zd'})

        driver.refresh()

        username = driver.find_element_by_class_name("user-name").text
        print(username)

        driver.quit()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    # unittest.main()
    # 装载测试用例
	test_cases = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
	# 使用测试套件并打包测试用例
	test_suit = unittest.TestSuite()
	test_suit.addTests(test_cases)
	# 运行测试套件，并返回测试结果
	test_result = unittest.TextTestRunner(verbosity=2).run(test_suit)
	#生成测试报告
	print("testsRun:%s" % test_result.testsRun)
	print("failures:%s" % len(test_result.failures))
	print("errors:%s" % len(test_result.errors))
	print("skipped:%s" % len(test_result.skipped))

def test_click_all_links_on_page(self):
	driver = self.driver
	driver.get("http://www.google.com")
	length = len(driver.find_elements_by_tag_name("a"))
	for i in range(0,length):
		links = driver.find_elements_by_tag_name("a")
	if links[i].is_displayed():
		links[i].click()
		driver.back()
	self.assertIn("Google" or "YouTube",driver.title)

def tearDown(self):
	self.driver.close()


# test case
# def testbrowser(driver):
#     driver.get("http://www.baidu.com")
#     driver.find_element_by_id("kw").click()
#     driver.find_element_by_id("kw").clear()
#     driver.find_element_by_id("kw").send_keys("vx")
#     driver.find_element_by_id("su").click()
#     driver.implicitly_wait(30)
#     time.sleep(3)
#     driver.close()
#     driver.quit()
#     return None

#不同浏览器兼容性
# driverfirefox = webdriver.Firefox()
# testbrowser(driverfirefox)

# driverie = webdriver.Ie()
# testbrowser(driverie)

# driverchrome = webdriver.Chrome()
# testbrowser(driverchrome)

#保存unitest输出日志
# log_file = "log_file.txt"
# f = open(log_file, "w")
# runner = unittest.TextTestRunner(stream=f,verbosity=2)
# unittest.main(exit = False,testRunner=runner)
# f.close()