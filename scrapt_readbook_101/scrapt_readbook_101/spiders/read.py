import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapt_readbook_101.items import ScraptReadbook101Item


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1188_1.html']

    rules = (
        Rule(LinkExtractor(allow=r'/book/1188_\d+\.html'),
             callback='parse_item',
             follow=False),
    )

    def parse_item(self, response):
        # item = {}
        img_list = response.xpath('//div[@class="bookslist"]//img')
        for img in img_list:
            src = img.xpath('./@data-original').extract_first()
            name = img.xpath('./@alt').extract_first()
            book = ScraptReadbook101Item(src=src, name=name)
            yield book
        # print('+++++++++++++++++++++++++++++++++++++++++++++')
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
