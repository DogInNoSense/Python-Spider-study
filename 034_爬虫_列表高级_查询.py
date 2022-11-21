# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 16:07
# @Author : www.lmxyz.xyz
# @File : 034_爬虫_列表高级_查询
# @Project : spider-study
food_list = ['锅包肉', '东北乱炖', '青椒肉']

food = input('请输入您想吃的食物')
# in
if food in food_list:
    print('在')
else:
    print('不在')

# not in
ball_list = ['蓝球', '台球']
ball = input('输入您喜欢的球类')

if ball not in ball_list:
    print('不在')
else:
    print('在')
