import scrapy

from scrapy_movie_099.items import ScrapyMovie099Item


class MvSpider(scrapy.Spider):
    name = 'mv'
    allowed_domains = ['m.dytt8.net']
    start_urls = ['https://m.dytt8.net/index2.htm']

    def parse(self, response):
        # print('============================')
        # 要第一页的名字和第二页的图片
        a_list = response.xpath('//div[@class="co_content8"]//tr//a[2]')
        for a in a_list:
            # a获取第一页的name和链接
            name = a.xpath('./text()').extract_first()
            href = a.xpath('./@href').extract_first()
            # print(name, href)
            # 第二页的地址是
            url = 'https://m.dytt8.net' + href
            # print(name, url)

            # 对第二页的链接发起访问 自己定义一个函数并且给他第二页的地址
            yield scrapy.Request(url=url, callback=self.parse_second, meta={'name': name})

    def parse_second(self, response):
        # print('1234567890')
        # '//div[@class="co_content8"]//span/img/@src'
        # 拿不到数据需检验xpath语法是否正确
        src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        # print(src)
        # 接收到请求的meta参数的值
        name = response.meta['name']
        print(name, src)
        # movie = ScrapyMovie099Item(src=src, name=name)
        # 将movie返回给管道
        # yield movie
