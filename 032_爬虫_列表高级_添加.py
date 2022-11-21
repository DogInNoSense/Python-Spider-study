# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 13:03
# @Author : www.lmxyz.xyz
# @File : 032_爬虫_列表高级_添加
# @Project : spider-study

# append 追加 在列表的最后添加
country_list = ['中国', '美国']
print(country_list)
country_list.append('俄罗斯')
print(country_list)

# insert index填想插入数据的下标
char_list = ['a', 'c', 'd']
char_list.insert(1, 'b')
print(char_list)

# extend 追加列表
num_list = [1, 2, 3]
num1_list = [4, 5, 6]
num_list.extend(num1_list)
print(num_list)
