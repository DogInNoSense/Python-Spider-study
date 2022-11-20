# _*_ coding : utf-8 _*_
# @Time : 2022/11/20 22:23
# @Author : www.lmxyz.xyz
# @File : 029_爬虫_流程控制语句_ifelse
# @Project : spider-study


try:
    score = int(input('请输入分数'))
    if score > 100 or score < 0:
        print('数据不符合要求')
    else:
        if score >= 90:
            print('优秀')
        elif score >= 80:
            print('良好')
        elif score >= 70:
            print('中等')
        elif score >= 60:
            print('及格')
        else:
            print('不及格')
except:
    print('数据不合法')
