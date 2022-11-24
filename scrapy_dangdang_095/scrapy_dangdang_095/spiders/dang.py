import scrapy


class DangSpider(scrapy.Spider):
    name = 'dang'
    allowed_domains = ['http://category.dangdang.com/cp01.27.02.00.00.00.html']
    start_urls = ['http://category.dangdang.com/cp01.27.02.00.00.00.html']

    def parse(self, response):
        print('********************************************')
        # items
        # '//ul[@id="component_59"]//li//img/@src'
        # '//ul[@id="component_59"]//li//img/@alt'
        # '//ul[@id="component_59"]//li//p[@class="price"]/span[1]/text()'
        # 所有的selector的对象都可以再次调用xpath方法

        li_list = response.xpath('//ul[@id="component_59"]//li')
        for li in li_list:
            # print(li)
            src = li.xpath('.//img/@data-original').extract_first()
            if src:
                src = src
            else:
                src = src = li.xpath('.//img/@src').extract_first()

            # 第一张图片和其他图片的标签属性不一样
            # 第一张图片的src是可以使用的,其他的是 data-original
            name = li.xpath('.//img/@alt').extract_first()
            price = li.xpath('.//p[@class="price"]/span[1]/text()').extract_first()
            print(src, name, price)
