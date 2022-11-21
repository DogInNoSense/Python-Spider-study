# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 18:54
# @Author : www.lmxyz.xyz
# @File : 041_爬虫_字典的高级_删除
# @Project : spider-study

# del
# 1.删除字典中指定的某一个元素
person = {'name': '老马', 'age': 18}
print(person)
del person['age']
print(person)
# 2.删除整个字典
# clear
del person
# print(person)   # 整个字典都删掉
# 3. 清空字典，但是保留字典对象
person.clear()
print(person)
