# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
import base64
import requests



class ProxyMiddleware(object):
    def get_proxy(self):
        proxylist = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=704c252a706b4598b60dd31b12655063&count=5&expiryDate=0&format=2&newLine=2"
        pro_addr = requests.get(proxylist).text
        print(pro_addr)
        IPs = pro_addr.split("\n")

        return IPs

    def get_random_ip(self):
        # proxylist = "http://piping.mogumiao.com/proxy/api/get_ip_al?appKey=704c252a706b4598b60dd31b12655063&count=3&expiryDate=0&format=2&newLine=2"
        # pro_addr = requests.get(proxylist).text
#        IPs = self.get_proxy()
        IPs = [
        '114.228.200.77:56416',

    ]
        proxyip = random.choices(IPs)
        print(str(proxyip))
        return proxyip

    def process_request(self, request, spider):
        ip = self.get_random_ip()
        print("Current IP:Port is %s" % ip)
        request.meta['proxy'] ="http://" + ip[0]

class UAMiddleware(object):
    ua_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Mozilla/5.0 (compatible; Baiduspider/2.0; - +http://www.baidu.com/search/spider.html)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
        'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
        'Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)',
    ]

    def process_request(self,request,spider):
        ua = random.choice(self.ua_list)
        request.headers['User-Agent'] = ua
        print(request.url)
        print(request.headers['User-Agent'])

    def process_response(self,request,response,spider):
        return response

    def process_exception(self,request,exception,spider):
        pass

class WandouSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
