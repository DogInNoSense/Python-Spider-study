# _*_ coding : utf-8 _*_
# @Time : 2022/11/20 21:01
# @Author : www.lmxyz.xyz
# @File : 016_爬虫_类型转换_转换为布尔类型
# @Project : spider-study

# 整数
# 如果 非0 的整数进行 bool 类型转换 则全是True
# a = -1
# b = bool(a)
# print(b)
# print(type(b))

# 浮点数 非 0 都是True
# 0.0 False

# a = -1.0
# b = bool(a)
# print(b)
# print(type(b))

# 字符串 有内容都返回 True, 没有内容返回 False

# a = '中国'
# b = bool(a)
# print(b)
# print(type(b))

# 列表 有内容都返回 True, 没有内容返回 False

# a = ['中国', '美国', '俄罗斯', '新加坡', '朝鲜']
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 元组 有内容都返回 True, 没有内容返回 False

# a = ('李逵', '林冲', '鲁智深', '武松', '潘金莲')
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# 字典 有内容都返回 True, 没有内容返回 False

a = {'name': 'xyz', 'age': '18'}
print(type(a))
b = bool(a)
print(b)
print(type(b))

# 什么情况是 False
print(bool(0))
print(bool(0.0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))
