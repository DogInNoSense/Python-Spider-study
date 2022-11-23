import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['https://car.autohome.com.cn/price/brand-15.html']
    # html结尾后面不能加/
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        # print('=======================')
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="lever-price red"]/span/text()')
        # print(name_list)
        # for name in name_list:
        #     print(name.extract())

        for index in range(len(name_list)):
            name = name_list[index].extract()
            price = price_list[index].extract()
            print(name, price)

# '//div[@class="main-lever"]//span/span/text()'
