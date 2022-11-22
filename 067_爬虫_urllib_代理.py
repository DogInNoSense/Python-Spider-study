# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 20:33
# @Author : www.lmxyz.xyz
# @File : 067_爬虫_urllib_代理
# @Project : spider-study
import urllib.request
import urllib.parse

url = 'https://www.baidu.com/s?wd='
data = urllib.parse.quote('我的ip')

url = url + data
print(url)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# # 模拟浏览器访问服务器
# response = urllib.request.urlopen(request)
proxies = {
    'http': '27.42.168.46:55481'
}

handler = urllib.request.ProxyHandler(proxies=proxies)
opener = urllib.request.build_opener(handler)
response = opener.open(request)
# 获取响应信息
content = response.read().decode('utf-8')

# 保存
with open('agt.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
