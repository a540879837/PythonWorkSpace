"""
Created on 2017年3月29日
@author: liaoxinyu
webdriver方法封装
简易封装定位单个元素和定位一组元素的方法
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import *
from selenium.webdriver.common.keys import *

'''定位单个元素'''
def findId(driver,id):
	f = driver.find_element_by_id(id)
	return f

def findName(driver,name):
	f = driver.find_element_by_name(name)
	return f

def findClassName(driver,name):
	f = driver,find_element_by_class_name(name)
	return f

def findTagName(driver,name):
	f = driver.find_element_by_tag_name(name)
	return f

def findLinkText(driver,text):
	f = driver.find_element_by_link_text(text)
	return f

def findPLinkText(driver,text):
	f = driver.find_element_by_partial_link_text(text)
	return f

def findXpath(driver,xpath):
	f = driver.find_element_by_xpath(xpath)
	return f

def findCss(driver,css):
	f = driver.find_element_by_css_selector(css)
	return f

'''定位一组元素'''
def findsId(driver,id):
	f = driver.find_elements_by_id(id)
	return f

def findsName(driver,name):
	f = driver.find_elements_by_name(name)
	return f

def findsClassName(driver,name):
	f = driver.find_elements_by_class_name(name)
	return

def findsTagName(driver,name):
	f = driver.find_elements_by_tag_name(name)

def findsLinkText(driver,text):
	f = driver.find_elements_by_link_text(text)
	return f

def findsPLinkText(driver,Text):
	f = driver.find_elements_by_partial_link_text(text)
	return f

def findsXpath(driver,xpath):
	f = driver.find_elements_by_xpath(xpath)
	return f

def findsCss(driver,css):
	f = driver.find_elements_by_css_selector(css)
	return f


'''鼠标事件'''
def contextClick(driver,element):
	f = ActionChains(driver).context_click(element).perform()
	return f
	#鼠标右键点击

def doubleClick(driver,element):
	f = ActionChains(driver).double_click(element).perform()
	return f
	#鼠标双击

def dragAndDrop(driver,element,target):
	f = ActionChains(driver).drag_and_drop(element, target).perform()
	return f
	#鼠标拖动element至target处

def clickAndHold(driver,element):
	f = ActionChains(driver).click_and_hold(element).perform()
	return f
	#按下鼠标左键

def moveMouse(driver,element):
	f = ActionChains(driver).move_to_element(element).perform()
	return f
	#移动鼠标至目标元素

#遍历指定目录，显示目录下的所有文件名
def eachFile(filepath):
	pathDir = os.listdir(filepath)
	for allDir in pathDir:
		articlesName = os.path.join('%s%s' % (filepath,allDir))
		print (txt.decode('gbk')) # .decode('gbk')是解决中文显示乱码问题

#读取文件内容并打印
def readFile(filename):
	List = []#定义一个List数组用于接收遍历后的内容
	f_open = open(filename,'r') #'r'代表只读权限权限
	for eachLine in f_open:
		# print ("读取每一行得到的内容：%s" % eachLine)
		List.append(eachLine)
	print(List)
	return List
	#返回List，用于外部使用本方法时接收
	f_open.close()

#输入多行文字，写入指定文件并保存到指定文件夹
def writeFile(filename):
	f_open = open(filename,'w')
	print("请输入多行文字,输入.号回车保存")
	while True:
		aLine = raw_input()
		if aLine != ".":
			f_open.write('%s%s' % (aLine, os.linesep))
		else:
			print("文件已保存！")
			break
		f_open.close()

# if __name__  = "__main__":
# 	filePath = "D:\\FileDemo\\Java\\myJava.txt"
# 	filePathI = "D:\\FileDemo\\Python\\pt.py"
# 	filePathC = "C:\\"
# 	eachFile(filePathC)
# 	readFile(filePath)
# 	writeFile(filePathI)