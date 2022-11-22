# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 21:43
# @Author : www.lmxyz.xyz
# @File : 070_爬虫_解析_xpath的基本使用
# @Project : spider-study

from lxml import etree

# xpath解析
# 1.本地文件
# 2.服务器响应的数据 response.read().decode('utf-8')


# 1.xpath 解析本地文件
tree = etree.parse('070_爬虫_解析_xpath的基本使用.html')
print(tree)

# tree.xpath('xpath路径')
# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# print(li_list)


# 查找所有id属性的li标签
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)
print(len(li_list))

print('-' * 10)

# 找到所有id为li的标签
li_list = tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list)
print(len(li_list))

print('-' * 10)
# 查找到id 为 l1的li标签的class的属性值
li = tree.xpath('//ul/li[@id="l1"]/@class')
print(li)
print(len(li))

print('-' * 10)
# 查询id中包含c的li标签
li_list = tree.xpath('//ul/li[contains(@id,"c")]/text()')
print(li_list)
print(len(li_list))

print('-' * 10)
# 查询id的值以l开头的li标签
li_list = tree.xpath('//ul/li[starts-with(@id,"l")]/text()')
print(li_list)
print(len(li_list))

print('-' * 10)
# 查询id为l1和class为c1的
li_list = tree.xpath('//ul/li[@id="l1" and @class="l1"]/text()')
print(li_list)
print(len(li_list))

print('-' * 10)
# 查询id为l1和或为l1的
li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
print(li_list)
print(len(li_list))
