# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 21:19
# @Author : www.lmxyz.xyz
# @File : 068_爬虫_urllib_代理池
# @Project : spider-study

import urllib.request
import random

proxies_pool = [
    {'http': '61.164.39.68:53281'},
    {'http': '183.236.232.160:8080'},
    {'http': '27.42.168.46:55481'},
    {'http': '61.216.185.88:60808'}
]

proxies = random.choice(proxies_pool)
print(proxies)
url = 'https://www.baidu.com/s?wd=ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')

# 保存
with open('agt1.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
