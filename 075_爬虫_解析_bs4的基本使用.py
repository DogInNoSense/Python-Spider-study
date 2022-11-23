# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 14:44
# @Author : www.lmxyz.xyz
# @File : 075_爬虫_解析_bs4的基本使用
# @Project : spider-study

# 安装
# pip install bs4
# pip install bs4 -i 国内源链接


# 导入 from bs4 import BeautifulSoup
from bs4 import BeautifulSoup

# 解析本地文件来学习bs4的基本语法
# 默认打开的文件的编码格式是gbk 所以在打开文件的时候需要指定编码
soup = BeautifulSoup(open('075_爬虫_解析_bs4的基本使用.html', encoding='utf-8'), 'lxml')
# print(soup)

# bs4的基本语法
# 根据标签名查找节点
# 找到的是第一个符合条件的数据
print(soup.a)
print('-' * 10)
# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# 1.find
print('-' * 10)
# 找到的是第一个符合条件的数据
print(soup.find('a'))
# 根据title的值找到对应的标签对象
print(soup.find('a', title="myblog"))
# 根据class的值找对应的标签对象 注意的是class_(加下划线)
print(soup.find('a', class_="site"))
# 2.fin_all
# 返回的是列表 所有的a标签
print('-' * 10)
print(soup.find_all('a'))
# 所有的a和span标签(需放到列表)
print('-' * 10)
print(soup.find_all(['a', 'span']))
# limit查找前几个数据
print(soup.find_all('li', limit=2))

# 3.select(推荐)
# select方法返回的是一个列表 并且会返回多个数据
print(soup.select('a'))
print('-' * 10)
# 根据类选择器寻找数据 .类名
print(soup.select('.site'))
# 根据id选择数据
print(soup.select('#l1'))
# 属性选择器
# 查找到li标签中有id的标签 列表形式输出
print('-' * 10)
print(soup.select('li[id]'))
# id为l2的
print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器
# 找div下面的li
print('-' * 10)
print(soup.select('div li'))
# 子代选择器
# 某标签的第一级标签
# 注意: 很多的计算机编程语言中 如果不加空格不会输入内容 但是bs4中不会报错,会显示内容
print(soup.select('div >ul >li'))

# 找到a标签和li标签的所有的对象
print(soup.select('a,li'))

# 节点信息
# 获取节点内容
print('-' * 10)
obj = soup.select('#d1')[0]
# 如果标签对象中 只有内容 那么string和get_text()都能获取数据
# 如果标签对象中 除了内容还有标签 那么string就获取不到数据
print(obj.string)
print(obj.get_text())

# 节点的属性
obj = soup.select('#p1')[0]
# name是标签的名字
print(obj.name)
# 将属性值作为一个字典返回
print(obj.attrs)

# 获取节点的属性
obj = soup.select('#p1')[0]
# 以下三种写法等价
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])  # 推荐第一种
