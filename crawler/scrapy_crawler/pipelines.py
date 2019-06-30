# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2

class CrawlerPipeline(object):
    def process_item(self, item, spider):
        return item

class QuotesPipeline(object):

    def open_spider(self, spider):
        hostname = 'db'
        username = 'admin'
        password = 'admin'
        database = 'smart'
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        self.cur = self.connection.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS crawled_result (short_title text, full_title text, arbitration_rules text, decisions_rendered text)")
        self.cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS pk_crawled_result_idx ON crawled_result (short_title)")
        self.connection.commit()
    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cur.execute(f"insert into crawled_result(short_title, full_title, arbitration_rules, decisions_rendered) values('{item['short_title']}','{item['full_title']}', '{item['arbitration_rules']}', '{item['decisions_rendered']}') ON CONFLICT DO NOTHING")
        self.connection.commit()
        return item
