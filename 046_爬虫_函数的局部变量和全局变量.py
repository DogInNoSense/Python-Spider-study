# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:21
# @Author : www.lmxyz.xyz
# @File : 046_爬虫_函数的局部变量和全局变量
# @Project : spider-study

def f1():
    a = 1
    print(a)


f1()
# print(a)

# 全局变量
# 可以函数的内部和外部使用
print('-' * 10)
a = 1


def f2():
    print(a)


print(a)
f2()
