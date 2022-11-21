# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 21:52
# @Author : www.lmxyz.xyz
# @File : 059_爬虫_urllib_post请求百度翻译
# @Project : spider-study

# post请求
import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# post 请求必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')

# post请求的参数是不会拼接在url后面的 而是需要放在请求对象定制的参数中
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode('utf-8')
print(content)
