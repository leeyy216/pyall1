# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from djanjc.items import DjanjcItem

class MyCrawlSpider(CrawlSpider):
    name = 'djanjc_crawler'               # Spider名，必须唯一，执行爬虫命令时使用
    allowed_domains = ['ziqiangxuetang.com']   # 限定允许爬的域名，可设置多个
    start_urls = [
        "http://www.ziqiangxuetang.com/django",       # 种子URL，可设置多个
    ]
    # rules = (    # 对应特定URL，设置解析函数，可设置多个
    #     Rule(LinkExtractor(allow=r'/django-[.*]+'),  # 指定允许继续爬取的URL格式，支持正则
    #                        callback='parse_item',   # 用于解析网页的回调函数名
    #                        follow=True
    #     ),
    # )

    def parse(self, response):
        # 通过XPath获取Dom元素
        title1 = response.xpath('//h1').extract()[0].encode('utf-8').decode('utf-8')
        title2 = response.xpath('//h1/span').extract()[0].encode('utf-8').decode('utf-8')
        item['title'] = title1 + title2
        articles = response.xpath("//article")
        for article in articles:
            item = DjanjcItem()
            item['url'] = article.xpath('header/h2/a/@href').extract()[0].encode('utf-8').decode('utf-8')
            item['summary'] = article.xpath('div/p/text()').extract()[0].encode('utf-8').decode('utf-8')
            yield item

    def parse_item(self, response):
        # 通过XPath获取Dom元素
        articles = response.xpath("//article")
        for article in articles:
            item = DjanjcItem()
            item['title'] = article.xpath('header/h2/a/text()').extract()[0]
            item['url'] = article.xpath('header/h2/a/@href').extract()[0]
            item['summary'] = article.xpath('div/p/text()').extract()[0]
            yield item