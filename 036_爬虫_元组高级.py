# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:18
# @Author : www.lmxyz.xyz
# @File : 036_爬虫_元组高级
# @Project : spider-study

a_tuple = (1, 2, 3, 4)
print(a_tuple[0])

# 元组不可以修改里面的内容
# a_tuple[3] = 5
# print(a_tuple)

# 列表中的元素可以修改

# 当元组中只有一个元素的时候  那么他是整型
b_tuple = (5)
print(type(b_tuple))

b_tuple = (5,)
print(type(b_tuple))  # <class 'tuple'>
