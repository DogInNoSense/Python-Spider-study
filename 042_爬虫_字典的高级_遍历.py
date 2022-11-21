# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:00
# @Author : www.lmxyz.xyz
# @File : 042_爬虫_字典的高级_遍历
# @Project : spider-study

person = {'name': '张三', 'age': 18, 'sex': 'male'}
# 遍历 key
for key in person.keys():
    print(key)
print('-------------------')

# 遍历字典的value
for value in person.values():
    print(value)

print('-------------------')
# 遍历字典的
for key, value in person.items():
    print(key, value)

print('-------------------')

# 遍历字典的项
for item in person.items():
    print(item)
