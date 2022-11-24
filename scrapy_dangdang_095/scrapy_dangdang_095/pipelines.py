# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 如果想使用管道 那么就必须在settings中开启管道
class ScrapyDangdang095Pipeline:
    # items  就是yield后面的book对象\
    # 爬虫开始之前执行
    def open_spider(self, spider):
        # print('********************************')
        self.fp = open('book.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # write必须要写一个字符串 而不能是其他对象
        # w模式 会覆盖之前的内容 要用 'a'追加
        # 以下这种模式不推荐 因为每传递过来一个对象 就打开一次文件 对文件的操作过于频繁
        # 不推荐
        # with open('book.json', 'a', encoding='utf-8') as fp:
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    #
    # # 爬虫执行完之后执行
    def close_spider(self, spider):
        # print('-----------------------------------')
        self.fp.close()


import urllib.request


#
#
# # 多条管道开启
# # 1.定义管道类
# # 2.在settings中开启管道
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        url = 'http:' + item.get('src')
        # 先新建好book文件夹
        filename = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=url, filename=filename)
        return item
