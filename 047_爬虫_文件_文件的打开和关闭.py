# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 19:25
# @Author : www.lmxyz.xyz
# @File : 047_爬虫_文件的打开和关闭
# @Project : spider-study

# 创建一个 test.txt文件
# 'w'可读
# 'r'可写
# fp = open('test.txt', 'w')
# fp.write('hello world')

# 打开文件
# fp = open('demo/text.txt', 'w')
# fp.write('hello www.lmxyz.xyz')

# 文件的关闭
fp = open('a.txt', 'w')
fp.write('hello')
# 必须要关闭释放资源
fp.close()
