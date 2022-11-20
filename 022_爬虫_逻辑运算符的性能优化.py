# _*_ coding : utf-8 _*_
# @Time : 2022/11/20 21:47
# @Author : www.lmxyz.xyz
# @File : 022_爬虫_逻辑运算符的性能优化
# @Project : spider-study

# 前面结果是False 后面结果不执行
# a = 36
# a > 10 and print('hello world')
# a < 10 and print('hello world')

# or 性能优化
b = 38
b > 39 or print('hello world')
b > 37 or print('hello world')  # 不会print
