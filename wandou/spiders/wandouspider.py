# -*- coding: utf-8 -*-
import scrapy
from ..items import WandouItem
from pyquery import PyQuery
import re

class WandouspiderSpider(scrapy.Spider):
    name = 'wandouspider'
    allowed_domains = ['www.wandoujia.com']
    start_urls = ['https://www.wandoujia.com/category/5018_597']

    def parse(self, response):
        item = WandouItem()
        jpy = PyQuery(response.text)
        print(response.text)
        li_list = jpy ('#j-tag-list > li').items()
        for it in li_list:
            strname = it('div.app-desc > h2 > a').text()
            strurl = it('div.app-desc > h2 > a').attr('href')
            print(strname)
            item['soft_name'] = strname
            item['soft_url'] = strurl
            yield item
        pass
