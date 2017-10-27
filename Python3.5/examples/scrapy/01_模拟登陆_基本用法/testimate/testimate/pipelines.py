# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
import pymongo
import sqlite3
import redis


# host=None, user=None, password="",
# database=None, port=0, unix_socket=None,
# charset='', sql_mode=None,
# read_default_file=None, conv=None, use_unicode=None,
# client_flag=0, cursorclass=Cursor, init_command=None,
# connect_timeout=10, ssl=None, read_default_group=None,
# compress=None, named_pipe=None, no_delay=None,
# autocommit=False, db=None, passwd=None, local_infile=False,
# max_allowed_packet=16*1024*1024, defer_connect=False,
# auth_plugin_map={}, read_timeout=None, write_timeout=None,
# bind_address=None):


class TestimatePipeline(object):
    def __init__(self):
        self.file = open('items.txt', 'w')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item


class SaveToMysqlPipeline(object):
    def __init__(self):
        self.config = {
            "host": "localhost",
            "user": "root",
            "password": "root",
            "database": "save_to_mysql",
            "port": 3306,
            "charset": "utf8"
        }
        self.conn = pymysql.connect(**self.config)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = "insert into article values(0, %s, %s, %s)"
        print(item)
        text = ""
        author = ""
        tag = ""
        for i in item["text"]:
            text += i + ','
        for i in item["author"]:
            author += i + ','
        for i in item["tag"][0]:
            tag += i + ','
        param_list = [text[:-2], author[:-2], tag[:-2]]
        print(param_list)
        count = self.cursor.execute(sql, param_list)
        print(count)
        for content in self.cursor.fetchall():
            print(content)
        self.conn.commit()
        # 存取数据结束时关闭
        # self.cursor.close()
        # self.conn.close()
        return item


# host = None,
# port = None,
# document_class = dict,
# tz_aware = None,
# connect = None,
# - `username`: A
# - `password`: A
class SaveToMongoPipeline(object):
    def __init__(self):
        self.config = {
            "host": "localhost",
            "port": 27017,
            # 设置数据库认证信息
            # "username": "root",
            # "password": "root"
        }
        self.client = pymongo.MongoClient(**self.config)
        self.db = self.client.save_to_mongo
        self.article = self.db.article

    def process_item(self, item, spider):
        try:
            print(item)
            new_item = dict()
            new_item['text'] = item["text"][0]
            new_item['author'] = item["author"][0]
            new_item['tag'] = item["tag"][0]
            self.article.insert_one(new_item)
            return item
        except Exception as e:
            print(e)


class SaveToSqlite3Pipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect("save_to_sqlite3.db")
        self.cursor = self.conn.cursor()
        sql = '''create table article
            (id integer primary key autoincrement not null,
                text varchar(200) not null,
                author varchar(200) not null,
                tag varchar(200) not null
            );'''
        self.cursor.execute(sql)
        self.conn.commit()

    def process_item(self, item, spider):
        sql = "insert into article(text, author, tag) values(?, ?, ?)"
        print(item)
        text = ""
        author = ""
        tag = ""
        for i in item["text"]:
            text += i + ','
        for i in item["author"]:
            author += i + ','
        for i in item["tag"][0]:
            tag += i + ','
        param_list = [text[:-2], author[:-2], tag[:-2]]
        print(param_list)
        count = self.cursor.execute(sql, param_list)
        print(count)
        for content in self.cursor.fetchall():
            print(content)
        self.conn.commit()
        # 存取数据结束时关闭
        # self.cursor.close()
        # self.conn.close()
        return item


class SaveToRedisPipeline(object):
    def __init__(self):

        # host = 'localhost', port = 6379,
        # db = 0, password = None, socket_timeout = None,
        # socket_connect_timeout = None,
        # socket_keepalive = None, socket_keepalive_options = None,
        # connection_pool = None, unix_socket_path = None,
        # encoding = 'utf-8', encoding_errors = 'strict',
        # charset = None, errors = None,
        # decode_responses = False, retry_on_timeout = False,
        # ssl = False, ssl_keyfile = None, ssl_certfile = None,
        # ssl_cert_reqs = None, ssl_ca_certs = None,
        # max_connections = None

        self.config = {
            "host": "localhost",
            "port": 6379,
            "db": 0
        }
        self.client = redis.StrictRedis(**self.config)

    def process_item(self, item, spider):
        # name, mapping
        try:
            print(item)
            new_item = dict()
            new_item['text'] = item["text"][0]
            new_item['author'] = item["author"][0]
            new_item['tag'] = item["tag"][0]
            # self.client.hmset('article', new_item)
            self.client.rpush('article', new_item)
            return item
        except Exception as e:
            print(e)
