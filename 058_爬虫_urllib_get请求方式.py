# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 21:41
# @Author : www.lmxyz.xyz
# @File : 058_爬虫_urllib_get请求方式
# @Project : spider-study
# import urllib.parse
#
# # urlencode: 多个参数的时候
# # https://www.baidu.com/s?wd=周杰伦&sex=男&location=中国台湾省
# data = {
#     'wd': '周杰伦',
#     'sex': '男',
#     'location': '中国台湾省'
# }
#
# a = urllib.parse.urlencode(data)
# print(a)

import urllib.request
import urllib.parse

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾省'
}

data = urllib.parse.urlencode(data)

# 请求资源路径
url = base_url + data
print(url)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码的数据
content = response.read().decode('utf-8')

# 打印数据
print(content)
