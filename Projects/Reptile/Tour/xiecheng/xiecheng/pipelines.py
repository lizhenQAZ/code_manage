# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class XiechengPipeline(object):
    def __init__(self):
        self.file = open("xiecheng_train.json", "wb")

    def process_item(self, item, spider):
        dict_data = dict(item)
        str_data = json.dumps(dict_data, ensure_ascii=False) + ",\n"
        self.file.write(str_data.encode())
        return item

    def __del__(self):
        self.file.close()
