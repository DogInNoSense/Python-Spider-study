import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字 用于运行爬虫的时候使用的值
    name = 'baidu'
    # 允许访问的域名
    allowed_domains = ['www.baidu.com']
    # 起始的url地址 第一次要访问的域名
    start_urls = ['http://www.baidu.com/']

    # 执行了start_urls之后的方法 方法中的response 就是返回的那个对象
    # 相当于response = urllib.request.urlopen()
    # response = requests.get()
    def parse(self, response):
        print('******************打印一次*********************')
