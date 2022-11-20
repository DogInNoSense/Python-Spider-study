# _*_ coding : utf-8 _*_
# @Time : 2022/11/20 22:34
# @Author : www.lmxyz.xyz
# @File : 030_爬虫_流程控制语句_for循环
# @Project : spider-study

# 循环字符串
# range(5)
# range(1,6)
# range(1,10,3)
# 循环一个列表

s = 'china'
for i in s:
    print(i)

# range(5): 0 ~ 4
for i in range(5):
    print(i)

# range(1,6) 1 2 3 4 5
# range(起始值,结束值)
for i in range(1, 6):
    print(i)

# range(1, 10, 3) 1 4 7
# range(起始值,结束值,步长)
for i in range(1, 10, 3):
    print(i)

# 应该场景 会爬取一个列表返回
a_list = ['周杰伦', '林俊杰', '陶喆']
# 遍历列表中的元素
for i in a_list:
    print(i)

# 遍历列表中的下标
for i in range(len(a_list)):
    print(i)
