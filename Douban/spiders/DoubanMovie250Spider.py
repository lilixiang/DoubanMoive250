#-*- coding: utf-8 -*-
'''

'''

from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Douban.items import DoubanItem

class DoubanMovie250Spider(CrawlSpider):
  # name of spiders
    name = 'douban'
    allow_domain = ['movie.douban.com']
    start_urls = [ 'http://movie.douban.com/top250' ]
    def parse(self, response):
        movie250 = DoubanItem()
        for sel in response.xpath('//ol[@class="grid_view"]/li'):
            movie250['rate'] = sel.xpath('//div[@class="pic"]/em/text()').extract()
            movie250['link'] = sel.xpath('//div[@class="pic"]/a/@href').extract()
            movie250['cover'] = sel.xpath('//div[@class="pic"]/a/img/@src').extract()
            movie250['title_cn'] = sel.xpath('//div[@class="hd"]/a/span[1]/text()').extract()
            movie250['title_en'] = sel.xpath('//div[@class="hd"]/a/span[2]/text()').extract()
            movie250['title_other'] = sel.xpath('//div[@class="hd"]/a/span[3]/text()').extract()
            movie250['introduction'] = sel.xpath('//div[@class="bd"]/p/text()').extract()
            movie250['star'] = sel.xpath('//div[@class="star"]/span[1]/em/text()').extract()
            movie250['value_p'] = sel.xpath('//div[@class="star"]/span[2]/text()').extract()
            movie250['quote'] = sel.xpath('//p[@class="quote"]/span[@class="inq"]/text()').extract()
            yield movie250
