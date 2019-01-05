# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WandouItem(scrapy.Item):
    soft_name = scrapy.Field()  # 软件名
    soft_url = scrapy.Field()   # 软件名URL
    pass
