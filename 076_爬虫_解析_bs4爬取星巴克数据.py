# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 16:18
# @Author : www.lmxyz.xyz
# @File : 076_爬虫_解析_bs4爬取星巴克数据
# @Project : spider-study
import urllib.request
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

# print(content)
soup = BeautifulSoup(content, 'lxml')

# //ul[@class="grid padded-3 product"]//strong/text()
name_list = soup.select('ul[class="grid padded-3 product"] strong')
for name in name_list:
    print(name.get_text())
