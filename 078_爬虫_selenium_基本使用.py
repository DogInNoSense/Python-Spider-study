# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 16:43
# @Author : www.lmxyz.xyz
# @File : 078_爬虫_selenium_基本使用
# @Project : spider-study

# https://chromedriver.storage.googleapis.com/index.html
# pip install selenium -i https://pypi.douban.com/simple

# 1. 导入  selenium
from selenium import webdriver

# 2. 创建浏览器操作对象

path = 'chromedriver.exe'

brower = webdriver.Chrome(path)

# 3. 访问网站
url = "https://www.jd.com/"

brower.get(url)
# page_source获取网页源码
content = brower.page_source
print(content)
# J_seckill
