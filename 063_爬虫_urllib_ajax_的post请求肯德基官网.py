# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 12:51
# @Author : www.lmxyz.xyz
# @File : 063_爬虫_urllib_ajax_的post请求肯德基官网
# @Project : spider-study

# 1页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post

# cname:
# 临沂
# pid:
# pageIndex:
# 1
# pageSize:
# 10


# 2页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# post

# cname:
# 临沂
# pid:
# pageIndex:
# 2
# pageSize:
# 10

import urllib.request
import urllib.parse

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}


def creat_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    data = {
        'cname': '临沂',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'

    }

    data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url=base_url, headers=headers, data=data)
    return request


def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


def download(content):
    with open('kfc_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    stat_page = int(input('请输入起始页:'))
    end_page = int(input('请输入结束页:'))

    for page in range(stat_page, end_page + 1):
        # print(page)
        # 请求对象的定制
        request = creat_request(page)
        # 获取网页源码
        content = get_content(request)
        download(content)
