# _*_ coding : utf-8 _*_
# @Time : 2022/11/22 15:53
# @Author : www.lmxyz.xyz
# @File : 065_爬虫_urllib_微博的cookie登录
# @Project : spider-study
import urllib.request

# 个人信息页面是utf-8 但是还是报编码错误  因为进入到了登陆页面(反爬手段)
# 登录页面不是utf-8
# 请求头的信息不够
# 使用的场景:数据采集的时候需要绕过登录 然后进入某个页面
url = 'https://weibo.com/u/5824884094'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Cookie': 'SUB=_2A25OePVODeRhGeFN6lEV8inKzjiIHXVtDGGGrDV8PUNbmtANLWz5kW9NQH5bAA6tuRhODJt8K8UsJoyVBVlMS_fA; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5JAbp1o70d_w7iBe2ikaSg5JpX5KzhUgL.FoM0eKeXeoMcSKB2dJLoIEXLxKML12-L12zLxKnL1h5L1h-LxKBLBonL12BLxK-L12qLB-qLxKnLBo5L12qt; WBPSESS=y9jd-BcqKKMv9rbK7sP8ExdbMOvuubPq7IH6VDc25CWNaKc_sE8HEslBhbLvbwaIBV917ignFT7F1yOpMU7NwtDtxsJfJPEEMxGQoipH5J6Cld3T0gF5gsHiGA23Lerso58bIncycq838-Joi4PRdA==; XSRF-TOKEN=T2xmy0WiLu6goTZH231zWnAo; ALF=1700640926; SSOLoginState=1669104926; _s_tentry=weibo.com; Apache=5392309035478.248.1669106825394; SINAGLOBAL=5392309035478.248.1669106825394; ULV=1669106825482:1:1:1:5392309035478.248.1669106825394:',
    'Referer': 'https://weibo.com/u/5824884094'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)
# 获取响应数据
content = response.read().decode('utf-8')
print(content)
# 保存本地
with open('weibo.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
