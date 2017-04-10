# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-30 09:05:44
# @Author  : liaoxinyu (2458006757@qq.com)
# @Link    : none
# @Version : kanQi_ManagementPlatform_public_login_v0.0.1T
# @Remarks : 文章搜索
# @platform : Windows

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time, re, os
import sys
sys.path.append(r"H:\\PythonWorkSpace\\MyTest")
from package import location

class KanQiArticlesSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.0.254/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kan_qi_articles_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("J-LoginUserName").clear()
        driver.find_element_by_id("J-LoginUserName").send_keys("廖欣宇")
        driver.find_element_by_id("J-LoginPwd").clear()
        driver.find_element_by_id("J-LoginPwd").send_keys("123456")
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"文章管理").click()
        time.sleep(1)
        driver.find_element_by_id("J-searchName").clear()

        lxy = location
        ArticleName = lxy.readFile(r"C:\\Users\\liaoxinyu\\Documents\\磨古\\看齐\\二期\\文章\\ArticleTitles.txt")
        #ArticleName接收readFile方法中return回的List
        for article_title in ArticleName:
            try:
                #循环ArticleName拿到ArticleTitles.txt中的每一个文章名
                searchTitle = driver.find_element_by_id("J-searchName")
                searchTitle.clear()
                searchTitle.send_keys(article_title)
                #清除搜索框已有的记录，并输入下一个文章名
                driver.find_element_by_xpath("//*[@id='J-searchBtn']/img").click()
                #点击搜索按钮
                time.sleep(0.3)
                searchR = WebDriverWait(driver, 2).until(lambda driver:driver.find_element_by_class_name("com-empty"))
                #2秒内持续寻找“暂无数据（searchR）”元素，未找到则抛异常
                # driver.find_element_by_class_name("com-empty")
                print(u"%s 没有搜索到\n" % article_title)
            except:
                print(u"%s 已搜索到\n" % article_title)
        driver.find_element_by_id("J-comLogoutBtn").click()
    
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
