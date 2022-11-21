# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 12:52
# @Author : www.lmxyz.xyz
# @File : 031_爬虫_字符串高级
# @Project : spider-study

# 获取长度 len
s = 'china'
print(len(s))

# 查找内容 find 返回字符位置
print(s.find('c'))

# 判断 是否 以..开头 start
print(s.startswith('c'))

# count 统计某些字符出现的次数
print(s.count('a'))

# replace 替换
print(s.replace('n', 'd'))
print(s)  # 原来字符串不变

# split 切割
s1 = '1#2#3#4#5'
print(s1.split('#'))

# upper 小写变大写
print(s.upper())

# lower 大写变小写
print(s.lower())

# strip 去空格
s2 = '    a    '
print(len(s2))
print(s2.strip(), len(s2.strip()))

# join 插入到字符串每一个元素后面
s3 = 'a'
print(s3.join('hello'))  # haealalao
