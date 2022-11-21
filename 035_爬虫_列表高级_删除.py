# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:14
# @Author : www.lmxyz.xyz
# @File : 035_爬虫_列表高级_删除
# @Project : spider-study

a_list = [1, 2, 3, 4, 5]
print(a_list)

# del
# 应用场景: 爬取的数据中有个别不想要的
del a_list[2]
print(a_list)

# pop 是删除列表中的最后一个元素
a_list.pop()
print(a_list)

# 根据元素来删除列表中的数据
a_list.remove(4)  # 删除元素4
print(a_list)
