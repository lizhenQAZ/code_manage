# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class DoubanPipeline(object):
    def __init__(self):
        self.file = open("douban.json", 'wb')
        # self.file.write('['.encode())

    def process_item(self, item, spider):
        movie_dict = dict(item)
        movie_str = json.dumps(movie_dict, ensure_ascii=False) + ',\n'
        self.file.write(movie_str.encode())
        return item

    def __del__(self):
        # self.file.write('{}]'.encode())
        self.file.close()
