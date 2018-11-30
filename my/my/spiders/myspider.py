# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from my.items import MyItem

class MyCrawlSpider(CrawlSpider):
    name = 'myspider'               # Spider名，必须唯一，执行爬虫命令时使用
    #allowed_domains = ['sqggfw.shmzj.gov.cn']   # 限定允许爬的域名，可设置多个
    start_urls = [
        "http://sqggfw.shmzj.gov.cn/Weixin/ItemList.aspx?ID=26",       # 种子URL，可设置多个
    ]

    def parse(self, response):
        # 通过XPath获取Dom元素
        for a in response.xpath("//a[@href]"):
            href = a.xpath("@href")
            url =  "http://sqggfw.shmzj.gov.cn/Weixin/" + href
            
        filename = 'b.xml'
        with open (filename, 'wb') as f:
            f.write(response.body)
