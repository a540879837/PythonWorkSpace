# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-30 09:05:44
# @Author  : liaoxinyu (2458006757@qq.com)
# @Link    : none
# @Version : kanQi_ManagementPlatform_public_login_v0.0.1T
# @Remarks : 登录接口测试
import requests
import json
from selenium import webdriver

url_login="http://192.168.0.254/kanqi_2.0_admin/admin/api/login"
url_aritcleList = "http://192.168.0.254/kanqi_2.0_admin/admin/api/recite/article/list"

userInfo = {'password':'123456','userName':'admin'}
headers = {'content-type':'application/json'}
logIn_InterF = requests.post(url_login,data = json.dumps(userInfo),headers = headers)
# print(logIn_InterF.headers)
cookieJ = logIn_InterF.cookies['JSESSIONID']
# print(cookieJ)


pageNum = {'pageNum':'1'}
article_list = requests.post(url_aritcleList,data = json.dumps(pageNum),headers = headers,cookies = {'JSESSIONID':cookieJ})
encodeJson = json.loads(article_list.text)

# data1 = {'a':789,'b':'123'}

# print(data1['a'])