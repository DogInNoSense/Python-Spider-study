# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 16:38
# @Author : www.lmxyz.xyz
# @File : 077_爬虫_selenium_为什么要学习_selenium
# @Project : spider-study

import urllib.request

url = 'https://www.jd.com/'

response = urllib.request.urlopen(url=url)

content = response.read().decode('utf-8')
print(content)
