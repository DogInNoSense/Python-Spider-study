# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 15:43
# @Author : www.lmxyz.xyz
# @File : 064_爬虫_urllib_异常
# @Project : spider-study
import urllib.request
import urllib.error

# url = 'https://blog.csdn.net/csdnnews/article/details/127977737?spm=1000.2115.3001.59270'
url = 'https:www.lmxyz.xyzz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
try:
    request = urllib.request.Request(url=url, headers=headers)

    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级..')
except urllib.error.URLError:
    print('系统还在升级...')
