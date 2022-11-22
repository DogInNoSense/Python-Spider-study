# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 16:59
# @Author : www.lmxyz.xyz
# @File : 066_爬虫_urllib_handler处理器的基本使用
# @Project : spider-study

# handler 定制高级的请求头
# 使用Handler来访问百度 获取网页源码
import urllib.request

url = 'http://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url, headers=headers)

# handler build_opener open
# 1.获取 handler 对象
handler = urllib.request.HTTPHandler()

# 2.获取 opener 对象

opener = urllib.request.build_opener(handler)

# 3.调用 open 方法
response = opener.open(request)

content = response.read().decode('utf-8')
print(content)
