# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 16:53
# @Author : www.lmxyz.xyz
# @File : 079_爬虫_selenium_元素定位
# @Project : spider-study

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'https://www.baidu.com'

browser.get(url)

# 元素定位

# 根据id找到对象
button = browser.find_element_by_id('su')
# print(button)

# 根据标签属性的属性值来获取对象的
button = browser.find_element_by_name('wd')
# print(button)

button = browser.find_elements_by_xpath('//input[@id="su"]')
# print(button)

# 根据标签名字获取对象
button = browser.find_elements_by_tag_name('input')
# print(button)

# 使用bs4的语法来获取对象
button = browser.find_elements_by_css_selector('#su')
# print(button)

# 获取链接文本
button = browser.find_element_by_link_text('地图')
print(button)
