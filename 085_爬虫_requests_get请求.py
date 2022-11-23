# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 21:29
# @Author : www.lmxyz.xyz
# @File : 085_爬虫_requests_get请求
# @Project : spider-study

# requests
# 1.一个类型以及六个属性
# 2.get请求
# 3.post请求
# 4.代理
# 5.cookie 验证码

import requests

url = 'https://www.baidu.com/s'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'wd': '北京'
}
# url请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url, params=data, headers=headers)
content = response.text
print(content)
