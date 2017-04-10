#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-30 09:05:44
# @Author  : liaoxinyu (2458006757@qq.com)
# @Link    : none
# @Version : kanQi_ManagementPlatform_public_login_v0.0.1T

import os,unittest,HTMLTestRunner,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
#导入封装好的方法
def login(self):
	driver = self.driver
	driver.maximize_window()
	# start logIn
	print("start login")
	user_name = driver.find_element_by_id("J-LoginUserName")
	user_name.clear()
	user_name.send_keys("admin")

	pass_word = driver.find_element_by_id("J-LoginPwd")
	pass_word.clear()
	pass_word.send_keys("123456")

	loginBtn = driver.find_element_by_link_text(u"登录")
	loginBtn.click()
	time.sleep(2)
    #end login
	print("end login")