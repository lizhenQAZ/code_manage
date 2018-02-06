# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from scrapy.pipelines.images import ImagesPipeline
from scrapy.conf import settings
import scrapy
import os


class Myspider006TuniuPipeline(object):
    def __init__(self):
        self.file = open("006tuniu.json", 'wb')

    def process_item(self, item, spider):
        str_data = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(str_data.encode())
        return item

    def __del__(self):
        self.file.close()


class Images(ImagesPipeline):
    IMAGES_STORE = settings['IMAGES_STORE']

    # 提交图片链接请求
    def get_media_requests(self, item, info):
        for img in item['image'].split('\n'):
            yield scrapy.Request(img)

    def item_completed(self, results, item, info):
        path = [data['path'] for status, data in results if status]
        item['image_path'] = self.IMAGES_STORE + os.sep + path[0]
        return item
