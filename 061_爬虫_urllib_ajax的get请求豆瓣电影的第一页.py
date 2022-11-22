# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 11:43
# @Author : www.lmxyz.xyz
# @File : 061_爬虫_urllib_ajax的get请求豆瓣电影的第一页
# @Project : spider-study

# get请求
# 获取豆瓣电影的第一页的数据 并且保存起来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 请求对象的定制

request = urllib.request.Request(url=url, headers=headers)

# 获取响应数据

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# 数据下载到本地
# open默认情况下使用的是gbk的编码 如果想要保存汉字 需要在open方法中指定编码格式为utf-8

# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)
# 等价于下面这种写法:
with open('douban.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
