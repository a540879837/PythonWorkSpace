#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-29 15:03:40
# @Author  : liaoxinyu (2458006757@qq.com)
# @Link    : none
# @Version : kanQi_Management platform_v0.0.1T

import unittest
import HTMLTestRunner
import os,time

listCase = 'H:\\PythonWorkSpace\\MyTest\\data'
def creatsuitel():
	testunit = unittest.TestSuite()

	#discover方法定义
	discover = unittest.defaultTestLoader.discover(listCase,
		pattern = 'kanQi_*.py',
		top_level_dir = None)

	#discover筛选出来的用例循环添加到测试套件中
	for test_suite in discover:
		for test_case in test_suite:
			testunit.addTest(test_case)
			print(testunit)
	return testunit

alltestnames = creatsuitel()

nowTime = time.strftime(r"%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filename = 'H:\\PythonWorkSpace\\MyTest\\report\\'+nowTime+'-result.html'
fp = open(filename,'wb')

runner = HTMLTestRunner.HTMLTestRunner(
	stream = fp,
	title = u'ArticlesInputReport',
	description = u'用例执行情况：')
runner.run(alltestnames)