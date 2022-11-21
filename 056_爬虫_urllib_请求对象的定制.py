# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 21:11
# @Author : www.lmxyz.xyz
# @File : 056_爬虫_urllib_请求对象的定制
# @Project : spider-study

import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://www.baidu.com/s?wd=周杰伦
# http/https www.baidu.com     80/443    s    wd = 周杰伦   #
# 协议          主机             端口号    路径   参数        锚点
# http: 80
# https: 443
# mysql: 3306
# oracle: 1521
# redis: 6379
# mongodb 27017

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)  # 参数顺序的问题，需要关键字传参
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
