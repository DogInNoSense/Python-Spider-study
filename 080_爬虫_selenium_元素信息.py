# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 17:18
# @Author : www.lmxyz.xyz
# @File : 080_爬虫_selenium_元素信息
# @Project : spider-study

from selenium import webdriver

path = 'chromedriver.exe'
browser = webdriver.Chrome(path)

url = 'http://www.baidu.com'

browser.get(url)

input = browser.find_element_by_id('su')
# 获取标签的属性
print(input.get_attribute('class'))
# 获取标签的名字
print(input.tag_name)

# 获取元素文本
a = browser.find_element_by_link_text('新闻')
print(a.text)
