# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 20:05
# @Author : www.lmxyz.xyz
# @File : 050_爬虫_异常
# @Project : spider-study


# 异常的格式
try:
    fp = open('test.txt', 'r')
    fp.read()
except FileNotFoundError:
    print('系统正在升级')
