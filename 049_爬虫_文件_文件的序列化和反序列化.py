# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:47
# @Author : www.lmxyz.xyz
# @File : 048_爬虫_文件_文件的序列化和反序列化
# @Project : spider-study
import json

# fp = open('test.txt', 'w')
# # 默认情况下我们只能将字符串写入到文件中
# fp.write('hell world')
# fp.close()


# # 序列化的2种方式
# fp = open('test.txt', 'w')
# # 默认情况 对象无法写入到文件中 如果想写入到文件 必须使用序列化操作
# name_list = ['zhangsan', 'lisi']
#
# # 导入json模块到文件中
# import json
#
# names = json.dumps(name_list)
# # 序列化
# # dumps
# fp.write(names)
# fp.close()

# dump
# 在将对象转换为字符串的同时 指定一个文件的对象 然后把转换后的字符串写入到文件里

# fp = open('test.txt', 'w')
# name_list = ['zs', 'ls']
# import json
#
# json.dump(name_list, fp)
# fp.close()

# 反序列化
# 将json的字符串变成一个python对象

# fp = open('test.txt', 'r')
# content = fp.read()
# print(content)
# print(type(content))
#
# import json
#
# print('-' * 10)
# # 将json字符串变成python对象
# loads
# result = json.loads(content)
# print(result)
# print(type(result))

fp = open('test.txt', 'r')
import json

result = json.load(fp)
print(result)
print(type(result))