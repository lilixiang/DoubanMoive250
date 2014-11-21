# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy
from scrapy.item import Item,Field


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rate = Field()
    link = Field()
    cover = Field()
    title_cn = Field()
    title_en = Field()
    title_other = Field()
    introduction = Field()
    star = Field()
    value_p = Field()
    quote = Field()
