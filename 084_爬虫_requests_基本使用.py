# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 21:22
# @Author : www.lmxyz.xyz
# @File : 084_爬虫_requests_基本使用
# @Project : spider-study

# 安装
# pip install requests
import requests

url = 'http://www.baidu.com'

response = requests.get(url=url)

# 一个类型和六个属性
print(type(response))  # Response类型

# 设置响应的编码格式
response.encoding = 'utf-8'

# 网页的源码
print(response.text)

# 返回url地址
print(response.url)

# 返回 的是二进制的数据
print(response.content)

# 返回响应的状态码
print(response.status_code)

# 返回响应头
print(response.headers)
