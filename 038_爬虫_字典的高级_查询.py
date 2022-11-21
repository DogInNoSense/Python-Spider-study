# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:27
# @Author : www.lmxyz.xyz
# @File : 038_爬虫_字典的高级
# @Project : spider-study

person = {'name': '张三', 'age': '18'}
# 访问person的name
print(person['name'])
print(person['age'])

# 获取字典中不存在的key的时候 (异常)
# print(person['sex'])


print(person.get('name'))
print(person.get('age'))
print(person.get('sex'))  # None
