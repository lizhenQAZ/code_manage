# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class Myspider002TencentPipeline(object):
    def __init__(self):
        self.file = open('002_tencent.json', 'wb+')

    def process_item(self, item, spider):
        dict_data = dict(item)
        str_data = json.dumps(dict_data, ensure_ascii=False) + ',\n'
        self.file.write(str_data.encode())

        return item

    def close_spider(self, spider):
        self.file.close()
