# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 21:04
# @Author : www.lmxyz.xyz
# @File : 082_爬虫_selenium_phantomjs的使用
# @Project : spider-study

# 无界面浏览器
# 不进行css和js渲染,效率更高

from selenium import webdriver

# 已经停止更新
path = 'phantomjs.exe'
browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)

# browser.save_screenshot('baidu.png')

import time

time.sleep(2)

input = browser.find_element_by_id('kw')
input.send_keys('周杰伦')

time.sleep(3)

browser.save_screenshot('周杰伦.png')
