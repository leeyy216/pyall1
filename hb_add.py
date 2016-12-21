# -*- coding: utf-8 -*-
import selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

import os


ff = webdriver.Firefox()

#ff.get("http://baidu.com")


class HbAdd(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://172.31.27.22:8088/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_hb_add(self):
        driver = self.driver
        driver.get(self.base_url + "/hbaq/system/homepage/show.do")
        driver.find_element_by_link_text(u"配置管理").click()
        driver.find_element_by_link_text(u"设备录入").click()
        driver.find_element_by_id("reset_v").click()
        Select(driver.find_element_by_id("type")).select_by_visible_text(u"虚拟机")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_link_text("fagag").click()
        driver.find_element_by_id("deviceName_v").clear()
        driver.find_element_by_id("deviceName_v").send_keys("lyytest5")
        driver.find_element_by_id("isPower1").click()
        driver.find_element_by_id("entityCode").clear()
        driver.find_element_by_id("entityCode").send_keys("123123")
        Select(driver.find_element_by_id("safetyDomain")).select_by_visible_text(u"网络交互域")
        driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
        driver.find_element_by_link_text("lyy tdtyku").click()
        driver.find_element_by_id("eniMacOne").clear()
        driver.find_element_by_id("eniMacOne").send_keys("11:11:11:11:11:11")
        driver.find_element_by_id("isOnline2").click()
        driver.find_element_by_id("isPower2").click()
        driver.find_element_by_id("isServer1").click()
        driver.find_element_by_id("onlineDate").click()
        driver.find_element_by_id("teturnTops").click()
 #      self.assertEqual(u"新增成功", self.close_alert_and_get_its_text())
        # ERROR: Caught exception [unknown command []]
    
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
        unittest.main()
