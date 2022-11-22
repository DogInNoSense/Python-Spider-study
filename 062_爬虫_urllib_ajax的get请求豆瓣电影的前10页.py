# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 11:56
# @Author : www.lmxyz.xyz
# @File : 062_爬虫_urllib_ajax的get请求豆瓣电影的前10页
# @Project : spider-study


# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=20&limit=20
# https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=40&limit=20


# get请求
# 获取豆瓣电影的第一页的数据 并且保存起来

import urllib.request
import urllib.parse

# 定制请求

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&'
    data = {
        'start': (page - 1) * 20,
        'limit': 20
    }
    data = urllib.parse.urlencode(data)
    url = base_url + data
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
    # print(content)


def download(page, content):
    with open('douban_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程序的入口
if __name__ == '__main__':
    stat_page = int(input('请输入起始的页码:'))
    end_page = int(input('请输入结束的页码:'))
    # 左闭右开
    for page in range(stat_page, end_page + 1):
        request = create_request(page)
        content = get_content(request)
        download(page, content)

    # headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
# }
#
# for index in range(10):
#     url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100:90&action=&start=' + str(
#         index * 20) + '&limit=20'
#     # 请求对象的定制
#     request = urllib.request.Request(url=url, headers=headers)
#     # 获取响应数据
#     response = urllib.request.urlopen(request)
#     content = response.read().decode('utf-8')
#     print(content)
#
#     with open('douban10.json', mode='a', encoding='utf-8') as fp:
#         fp.write(content)
