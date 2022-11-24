import scrapy
import json


class TestpostSpider(scrapy.Spider):
    name = 'testpost'
    allowed_domains = ['fanyi.baidu.com']
    # post请求如果没有参数 那么这个请求没有意义
    # start_url 也没用 parse方法也没用了
    start_urls = ['https://fanyi.baidu.com/sug']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'final'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        # print(content)
        obj = json.loads(content, encoding='utf-8')
        print(obj)
