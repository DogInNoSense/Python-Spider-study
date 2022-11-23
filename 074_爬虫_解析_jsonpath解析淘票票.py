# _*_ coding : utf-8 _*_
# @Time : 2022/11/23 14:10
# @Author : www.lmxyz.xyz
# @File : 074_爬虫_解析_jsonpath解析淘票票
# @Project : spider-study

import urllib.request

url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1669185021325_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': ' dianying.taobao.com',
    # ':method': ' GET',
    # ':path': ' /cityAction.json?activityId&_ksTS=1669183952980_104&jsoncallback=jsonp105&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'bx-v': '2.2.3',
    'cookie': 'cna=zou0G7/t8jgCAXAIKvWWsiTC; tracknick=%5Cu7AF9%5Cu9708%5Cu5D0E; thw=cn; miid=8548280241214742270; sgcookie=E100oWpdmOTKNE7s%2BiXhpJBotHN%2Bc0I%2FH0QFhm%2FO32q8QrFfdo5eyaG4W6WoXJUtUDQFem%2FZ1M3VAfA7eMLoZuAZYbt0E%2FeeIn55ivVF2rTrJQRYttVwyMOAaPCUXLLSMJT5; _cc_=UtASsssmfA%3D%3D; enc=vqvySnkGDHa8voTiXG2wYvSJZciQehkGVpb6T3rUSiHDGVaaP6uxbJRSJp4lKRDeZBupMshU3whTBBcyKu36Pw%3D%3D; tfstk=cDDPB_cVHLpy31mpW-2EQLeYkLiRZeMipZrQZe4dRWe5FrVliX_LmtDTg5sV-7f..; t=0030008cd30a22ba79144429d4f4ad74; _m_h5_tk=5d07d6d9f1939c85c78a5c6135c3ef61_1668790725004; _m_h5_tk_enc=c3549d681f4ee6e35bde4bdb4a00147e; cookie2=133e41e5fd12e105eced083bab32fb5d; v=0; _tb_token_=83b138b54e53; tb_city=110100; tb_cityName="sbG+qQ=="; l=eBQ6Vei7TSKlbapWBOfalurza779HIRbYuPzaNbMiOCPOLCH5eH1W6zBwJTMCn1VH6W2R3r0glSeB_hWVydNVcYON7h1WnfS3dC..; isg=BPn5l5a0vpX-emJSGrNyn8iBCGXTBu24ydtYwRsuByCfohg0Y1aGiZ_8JCZUAYXw',
    'referer': 'https://dianying.taobao.com/?spm=a1z21.3046609.city.1.32c0112a9wAHVH&city=110100',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')
# print(content)

# 切割
content = content.split('(')[1].split(')')[0]
# print(content)

# 只能解析本地数据,先保存
with open('074_爬虫_解析_jsonpath解析淘票票.json', 'w', encoding='utf-8') as fp:
    fp.write(content)

import json
import jsonpath

obj = json.load(open('074_爬虫_解析_jsonpath解析淘票票.json', 'r', encoding='utf-8'))
city_list = jsonpath.jsonpath(obj, '$..regionName')
print(city_list)
