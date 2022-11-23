import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://linyi.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&button=%E6%90%9C%C2%A0%E7%B4%A2']
    start_urls = ['https://linyi.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&button=%E6%90%9C%C2%A0%E7%B4%A2']

    def parse(self, response):
        # 字符串
        # content = response.text
        # 获取的是二进制数据
        # content = response.body
        # print('******************打印一次*********************')
        # print(content)
        span = response.xpath('//div[@id="filter"]/div[@class="tabs"]/a/span')[0]
        print('================================================')
        # print(span)
        print(span.extract())
