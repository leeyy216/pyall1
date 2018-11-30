# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
from selenium.webdriver.common.action_chains import ActionChains


'''
iedriver="C:\Program Files\Internet Explorer\IEDriverServer.exe"
os.environ["webdriver.ie.driver"] = iedriver
dri = webdriver.Ie(iedriver)
dri.get("https://www.baidu.com")

ff = webdriver.Ie(iedriver)
webdriver.ff
'''


# ffdriver = "D:\Program Files (x86)\Mozilla Firefox\geckodriver.exe"
# os.environ["webdriver.firefox.driver"] = ffdriver
# ff = webdriver.Firefox()

# # 一个测试用例
# class BaiduTest(unittest.TestCase):
#     def setUp(self):
#         iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
#         os.environ["webdriver.ie.driver"] = iedriver
#         self.driver = webdriver.Ie(iedriver)
#         # self.driver = webdriver.Firefox()
#         self.driver.implicitly_wait(30)
#         self.base_url = "https://www.baidu.com/"
#         self.verificationErrors = []
#         self.accept_next_alert = True
#
#     def test_Baidu_Login(self):
#
#         #打开浏览器，打开网页
#         driver = self.driver
#         driver.get(self.base_url)
#
#         #用cookie越过验证码登陆：（先打开网页），添加cookie，刷新，应变成登陆状态（验证：页面上登录的位置应显示用户名，获取用户名并输出）
#         # driver.add_cookie({'name': 'BAIDUID', 'value': 'B29D17367E8521A4E2BA0BFE9A7E67F1:FG=1'})
#         # driver.add_cookie({'name': 'BAIDUID', 'value': '402E56B216142E97AF5559174FD8582A:FG=1'})
#         # driver.add_cookie({'name': 'BDUSS',
#         #                    'value': 'NMQmZ5YW1NLVJjeTZ3cVg2T1lmdktxN2RDMWZZVHRTbGhFeFY3bS01SjR4RzVaSVFBQUFBJCQAAAAAAAAAAAEAAABztkYCa2VhaWxpemk2MTUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHg3R1l4N0dZTT'})
#         # driver.refresh()
#         # username = driver.find_element_by_class_name("user-name").text
#         # print(username)
#
#         #首页点击贴吧链接，弹出新选项卡贴吧首页，输入lovelive国服，点击进入贴吧
#         driver.find_element_by_link_text(u"贴吧").click()
#         time.sleep(5)
#         window_1 = driver.current_window_handle
#         windows = driver.window_handles
#         driver.switch_to.window(windows[-1])
#         time.sleep(5)
#         print (driver.title)
#         driver.find_element_by_id("wd1").send_keys("lovelive国服")
#         driver.find_element_by_link_text(u"进入贴吧").click()
#         time.sleep(5)
#         print(driver.title)
#
#         #切换回首页窗口，鼠标移至用户名，显示下拉菜单，点击菜单中的退出
#         # driver.switch_to.window(window_1)
#         # move_mouse = driver.find_element_by_class_name("user-name")
#         # ActionChains(driver).move_to_element(move_mouse).perform()
#         #
#         # driver.find_element_by_link_text("退出").click()
#         # driver.find_element_by_link_text("确定").click()
#         # 20170615 1702完成打开ie-进入百度-越过验证码登陆-鼠标悬浮到用户名-点击下拉菜单中的退出
#
#         # 切换回首页窗口，鼠标移至设置，显示下拉菜单，点击菜单中的搜索历史
#         driver.switch_to.window(window_1)
#         move_mouse = driver.find_element_by_name("tj_settingicon")
#         ActionChains(driver).move_to_element(move_mouse).perform()
#
#         driver.find_element_by_link_text("搜索历史").click()
#         driver.find_element_by_link_text("确定").click()


        # driver.quit()
        # BAIDUID=
        # 181E694A9DDCB85410C73B323E1AD3E4:FG=1
        # BDUSS=WVhUFBvTjRLY2NGQ2JzNjZXcU9TY05YUE1WV01uaFVEUTBjSll6anQwVy14V1ZaSVFBQUFBJCQAAAAAAAAAAAEAAABztkYCa2VhaWxpemk2MTUzAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL44Plm-OD5Zd

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
        #      self.assertEqual(u"新增成功", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [unknown command []]
class Teat_163(unittest.TestCase):
    def setUp(self):
        iedriver = "C:\Program Files\Internet Explorer\IEDriverServer.exe"
        os.environ["webdriver.ie.driver"] = iedriver
        self.driver = webdriver.Ie(iedriver)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://mail.163.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_163(self):
        driver = self.driver
        driver.get(self.base_url)

        driver.find_element_by_xpath("//input[@name='email']").send_keys("liyy9502")
        # driver.find_element_by_name("email").send_keys("liyy9502") 找不到元素
        driver.find_element_by_xpath("//input[@name='password']").send_keys("liyy9502")
        # driver.find_element_by_name("password").send_keys("LyyLee216")
        driver.find_element_by_id("dologin").click()

        time.sleep(5)

        driver.find_element_by_partial_link_text("写 信")
        time.sleep(3)
        driver.find_element_by_class_name("nui-editableAddr-ipt").sendkeys("627088113@qq.com")
        driver.find_element_by_class_name("nui-ipt-input").sendkeys("test selenium")
        driver.find_element_by_class_name("nui-scroll").sendkeys("test selenium123阿士大夫贺卡机顶盒番茄~！@#￥%……&*（）")
        driver.find_element_by_link_text("发送")



# def is_element_present(self, how, what):
#         try: self.driver.find_element(by=how, value=what)
#         except NoSuchElementException as e: return False
#         return True
#
#     def is_alert_present(self):
#         try: self.driver.switch_to_alert()
#         except NoAlertPresentException as e: return False
#         return True
#
#     def close_alert_and_get_its_text(self):
#         try:
#             alert = self.driver.switch_to_alert()
#             alert_text = alert.text
#             if self.accept_next_alert:
#                 alert.accept()
#             else:
#                 alert.dismiss()
#             return alert_text
#         finally: self.accept_next_alert = True
#
#     def tearDown(self):
#         self.driver.quit()
#         self.assertEqual([], self.verificationErrors)
#
if __name__ == "__main__":
    unittest.main()

