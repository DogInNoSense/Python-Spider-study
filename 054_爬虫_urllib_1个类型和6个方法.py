# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 20:52
# @Author : www.lmxyz.xyz
# @File : 054_爬虫_urllib_1个类型和6个方法
# @Project : spider-study

import urllib.request

url = 'http://www.baidu.com'
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和6个方法
# HTTPResponse类型
print(type(response))
# 按照一个字节一个字节的去读
# content = response.read(5)  # 返回5个字节
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 一行一行去读 直到读完
content = response.readlines()
print(content)

# 返回状态码 如果是200就证明逻辑没有错
print(response.getcode())

# 返回url地址
print(response.geturl())

# 获取的是一些状态信息
print(response.getheaders())
