# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 22:18
# @Author : www.lmxyz.xyz
# @File : 088_爬虫_requests_代理
# @Project : spider-study


# 通过登录 然后进入到主页面
# https://www.gushiwen.cn/


# __VIEWSTATE:  wIdWMYCT2ie70gQNEgYoN4AkkFt6yHaWlnz8OSCiYjiHN0Ggmb7py79olvd/8LyK/JjK9SfaClD7hQWlkMWHukGLFMiKnWT9My7AKjJ/PaJI/pG2E/fUjTjlEZ55FArHZc60/ZKiDBNWZ41xFovpPNJ4AQE=
# __VIEWSTATEGENERATOR: C93BE1AE
# from: http://so.gushiwen.cn/user/collect.aspx
# email: xie@gmail.com
# pwd: 1111111
# code: 77z5
# denglu:  登录

# __VIEWSTATE
# __VIEWSTATEGENERATOR
# 在页面的源码中

import requests

# 登录页面的url地址
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 获取网页的源码
response = requests.get(url=url, headers=headers)
content = response.text
# print(content)

# 解析页面源码 获取  __VIEWSTATE __VIEWSTATEGENERATOR
from bs4 import BeautifulSoup

soup = BeautifulSoup(content, 'lxml')

# 获取  __VIEWSTATE

viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')

# 获取 __VIEWSTATEGENERATOR
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

# print(viewstate)
# print(viewstategenerator)

# 获取验证码图片
code = soup.select('#imgCode')[0].attrs.get('src')
# print(code)
code_url = 'https://so.gushiwen.cn' + code
print(code_url)
# import urllib.request
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# requests里面的 session()方法
session = requests.session()
# 验证码url的内容
response_code = session.get(code_url)
# 获取图片的二进制数据
content_code = response_code.content
# wb的模式就是将二进制数据写入文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
# 获取到验证码之后 下载到本地 然后在控制台输入
code_name = input('请输入您的验证码')

# 点击登录
url_post = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
data_post = {
    '__VIEWSTATE': viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '19841358929',
    'pwd': '444455555.',
    'code': code_name,
    'denglu': '登录'
}

response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('guishiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
