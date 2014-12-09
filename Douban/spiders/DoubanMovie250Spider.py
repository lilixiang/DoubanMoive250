#-*- coding: utf-8 -*-

'''

'''

from scrapy.selector import Selector
from scrapy.http import  Request
from scrapy.contrib.spiders import CrawlSpider
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from Douban.items import DoubanItem
import urlparse,scrapy

class DoubanMovie250Spider(CrawlSpider):
  # name of spiders
    name = 'douban'
    allow_domain = ['movie.douban.com']
    start_urls = [ 'http://movie.douban.com/top250' ]
    def parse(self, response):
        movie250 = DoubanItem()
        results = response.xpath('//ol[@class="grid_view"]/li/div[@class="item"]')
        for result in results :
            movie250['rate'] = result.xpath('div[@class="pic"]/em/text()').extract()
            movie250['link'] = result.xpath('div[@class="pic"]/a/@href').extract()
            movie250['cover'] = result.xpath('div[@class="pic"]/a/img/@src').extract()
            movie250['title_cn'] = result.xpath('*/div[@class="hd"]/a/span[1]/text()').extract()
            movie250['title_en'] = result.xpath('*/div[@class="hd"]/a/span[2]/text()').extract()
            movie250['title_other'] = result.xpath('*/div[@class="hd"]/a/span[3]/text()').extract()
            movie250['introduction'] = result.xpath('*/div[@class="bd"]/p/text()').extract()
            movie250['star'] = result.xpath('*/div[@class="bd"]/div[@class="star"]/span[1]/em/text()').extract()
            movie250['value_p'] = result.xpath('*/div[@class="bd"]/div[@class="star"]/span[2]/text()').extract()
            movie250['quote'] = result.xpath('*/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()').extract() 

            yield movie250
        next_page = response.xpath('//*[@id="content"]//div[@class="paginator"]/span[@class="next"]/link/@href').extract()
        
        if next_page:            
            next_page = urlparse.urljoin(u'http://movie.douban.com/top250',next_page[0])
            yield Request(next_page, callback=self.parse)
