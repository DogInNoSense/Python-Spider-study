# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:51
# @Author : www.lmxyz.xyz
# @File : 39_爬虫_字典的高级_修改
# @Project : spider-study

# 修改
person = {'name': '张三', 'age': 19}
print(person)
# 键如果不存在就会变成新增元素（存在则修改）
person['name'] = '李四'
print(person)
