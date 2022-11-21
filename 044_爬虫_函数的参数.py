# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:10
# @Author : www.lmxyz.xyz
# @File : 044_爬虫_函数的定义和调用
# @Project : spider-study

# 计算 1 和 2 的和
def s():
    a = 1
    b = 2
    c = a + b
    print(c)


s()
print('-' * 10)


def s1(a, b):
    c = a + b
    print(c)


# 位置参数
s1(3, 2)

# 关键字传参
s1(b=200, a=100)
# 定义函数 s(a,b) a和b为形参
# 调用函数 s(3,2) 3和2为实参
