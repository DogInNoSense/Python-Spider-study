# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 20:30
# @Author : www.lmxyz.xyz
# @File : 053_爬虫_urllib_基本使用
# @Project : spider-study
import urllib.request

# 使用urllib爬取百度首页的源码

# 1.定义一个url 即访问地址

url = 'http://www.baidu.com'

# 2.模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 3.获取响应中的页面的源码
# read方法 返回的是字节形式的二进制数据
# content = response.read()
# print(content)
# 将二进制的数据转换为字符串
content = response.read().decode('utf-8')
print(content)
# 4.打印数据
