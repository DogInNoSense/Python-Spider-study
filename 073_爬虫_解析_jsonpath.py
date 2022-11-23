# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 13:24
# @Author : www.lmxyz.xyz
# @File : 073_爬虫_解析_jsonpath
# @Project : spider-study

# 资源下载链接
# https://blog.csdn.net/luxideyao/article/details/77802389
import json
import jsonpath

obj = json.load(open('073_爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))
# print(obj)
# 书店所有书的作者 (所有)

author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')  # book[*] 所有作者 book[0] 第一个
print(author_list)

# 所有的作者
author_list = jsonpath.jsonpath(obj, '$..author')
print(author_list)

# store下面所有的元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

print('-' * 10)
# store里面所有的price
price_list = jsonpath.jsonpath(obj, '$.store..price')
print(price_list)

# 第三个书
book = jsonpath.jsonpath(obj, '$..book[2]')
print(book)

# 最后一本书

last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(last_book)

print('-' * 10)
# 前两本书
pre_twobook = jsonpath.jsonpath(obj, '$..book[0,1]')
print(pre_twobook)

print('-' * 10)
# 过滤 所有的包含isbn的书
isbn_list = jsonpath.jsonpath(obj, '$..book[?(@.isbn)]')
print(isbn_list)

print('-' * 10)
# 过滤哪本书超过了10元
over_list = jsonpath.jsonpath(obj, '$..book[?(@.price>10)]')
print(over_list)
