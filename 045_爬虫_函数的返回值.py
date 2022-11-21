# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:17
# @Author : www.lmxyz.xyz
# @File : 045_爬虫_函数的返回值
# @Project : spider-study

def buyIceCream():
    return '冰激凌'


# 变量接收函数的返回值
food = buyIceCream()
print(food)


# 计算结果返回

def sum(a, b):
    c = a + b
    return c


value = sum(123, 456)
print(value)
