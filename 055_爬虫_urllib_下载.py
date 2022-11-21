# _*_ coding : utf-8 _*_
# @Time : 2022/11/21 21:01
# @Author : www.lmxyz.xyz
# @File : 055_爬虫_urllib_下载
# @Project : spider-study
import urllib.request

# 下载网页
url_page = 'http://www.baidu.com'
# url代表的是下载的路径 filename 文件的名字
urllib.request.urlretrieve(url_page, 'baidu.html')

# 下载图片
url_img = 'https://www.lmxyz.xyz/git-q/1.png'
urllib.request.urlretrieve(url_img, '1.png')

# 下载视频
url_video = 'https://vd3.bdstatic.com/mda-nkhfi4ftarpj7wh3/sc/cae_h264/1668769582289866567/mda-nkhfi4ftarpj7wh3.mp4?v_from_s=hkapp-haokan-suzhou&auth_key=1669037967-0-0-d38694dc99cbdd4130b4ed3f65fd0c5e&bcevod_channel=searchbox_feed&cd=0&pd=1&pt=3&logid=0567337349&vid=9604542498719615167&abtest=105568_1&klogid=0567337349'
urllib.request.urlretrieve(url_video, '1.mp4')
