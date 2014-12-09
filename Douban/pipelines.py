# -*- coding: utf-8 -*-
# Define your item pipelines here
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals
from scrapy import log
from Douban.items import DoubanItem
from twisted.enterprise import adbapi
from scrapy.contrib.exporter import JsonItemExporter
import codecs
class DoubanjsonPipeline(object):
    def __init__(self):
        pass
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        return pipeline
    def spider_opened(self, spider):
        self.file = codecs.open('douban250.json', 'wb','utf-8')
        self.expoter = JsonItemExporter(self.file, ensure_ascii=False)
        self.expoter.start_exporting()
    def spider_closed(self, spider):
        self.expoter.finish_exporting()
        self.file.close()
        # process the crawled data, define and call dataProcess function
        # dataProcess('bbsData.xml', 'text.txt')
    def process_item(self, item, spider):
        self.expoter.export_item(item)
        return item


