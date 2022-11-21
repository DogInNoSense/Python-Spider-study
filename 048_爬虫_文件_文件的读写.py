# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:36
# @Author : www.lmxyz.xyz
# @File : 048_爬虫_文件_文件的读写
# @Project : spider-study

# 写数据
# write方法

# fp = open('test.txt', 'w')
# 覆盖原来数据
# fp.write('hello world\n' * 5)

# 读数据
fp = open('test.txt', 'r')
# 默认情况下 read是一字节一字节的读效率比较低
# content = fp.read()
# print(content)

# 读取一行
content = fp.readline()
print(content)

# 读取多行
content = fp.readlines()
print(content)
