# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 22:16
# @Author : www.lmxyz.xyz
# @File : 072_爬虫_解析_站长素材
# @Project : spider-study

# 1.请求对象的定制
# 2.获取网页的源码
# 3.下载

# 下载前10页的图片
# https://sc.chinaz.com/tupian/huangsetupian.html
# https://sc.chinaz.com/tupian/huangsetupian_2.html


# https://sc.chinaz.com/tupian/page.html
import urllib.request
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/huangsetupian.html'
    else:
        url = 'https://sc.chinaz.com/tupian/huangsetupian_' + str(page) + '.html'
    # print(url)
    request = urllib.request.Request(url=url, headers=headers)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    # 下载图片
    tree = etree.HTML(content)
    # print(content)

    # 解析
    name_list = tree.xpath('//div[@class="container"]//div/img/@alt')
    # 一般涉及到图片的网站都会懒加载
    src_list = tree.xpath('//div[@class="container"]//div/img/@data-original')

    # 打印测试是否有数据
    # print(len(name_list))
    # for name in name_list:
    #     print(name)

    # for src in src_list:
    #     print(src)
    # print(len(src_list))

    for index in range(len(name_list)):
        name = name_list[index]
        src = src_list[index]
        url = 'https:' + src
        print(name, url)
        # 注意 filename='./yellow_img/' 后面还有一个/
        urllib.request.urlretrieve(url=url, filename='./yellow_img/' + name + '.jpg')


if __name__ == '__main__':
    stat_page = int(input('请输入起始页码:'))
    end_page = int(input('请输入结束页码:'))

    for page in range(stat_page, end_page + 1):
        # 1.请求对象的定制
        request = create_request(page)
        content = get_content(request)
        # print(content)
        download(content)
