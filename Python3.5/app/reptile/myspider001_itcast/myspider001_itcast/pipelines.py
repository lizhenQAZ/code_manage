# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Myspider001ItcastPipeline(object):
    def open_spider(self, spider):
        self.file = open('001_itcast.json', 'wb+')

    def process_item(self, item, spider):
        str_dict = json.dumps(item, ensure_ascii=False) + ',\n'
        self.file.write(str_dict.encode())
        return item

    def close_spider(self, spider):
        self.file.close()
