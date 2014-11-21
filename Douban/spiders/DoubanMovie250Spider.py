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
            movie250['rate'] = sel.xpath('div/div[@class="pic"]/em/text()').extract()
            movie250['link'] = sel.xpath('div/div[@class="pic"]/a/@href').extract()
            movie250['cover'] = sel.xpath('div/div[@class="pic"]/a/img/@src').extract()
            movie250['title_cn'] = sel.xpath('div/div[@class="info"]/div[@class="hd"]/a/span/text()').extract()
            movie250['title_en'] = sel.xpath('div/div[@class="info"]/div[@class="hd"]/a/span/text()').extract()
            movie250['title_other'] = sel.xpath('div/div[@class="info"]/div[@class="hd"]/a/span[@class="other"]/text()').extract()
            movie250['introduction'] = sel.xpath('div/div[@class="info"]/div[@class="bd"]/p/text()').extract()
            movie250['star'] = sel.xpath('div/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
            movie250['value_p'] = sel.xpath('div/div[@class="info"]/div[@class="bd"]/div[@class="star"]/span/em/text()').extract()
            movie250['quote'] = sel.xpath('div/div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract()
            yield movie250
