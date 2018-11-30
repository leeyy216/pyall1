# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from zkrx.items import ZkrxItem

class MyCrawlSpider(CrawlSpider):
    name = 'zkrx_spider'               # Spider名，必须唯一，执行爬虫命令时使用
    allowed_domains = ['shmeea.edu.cn']   # 限定允许爬的域名，可设置多个
    start_urls = [
        "http://www.shmeea.edu.cn/20150603/20150603.htm",       # 种子URL，可设置多个
    ]
    # rules = (    # 对应特定URL，设置解析函数，可设置多个
    #     Rule(LinkExtractor(allow=r'/page/[2-9]+'),  # 指定允许继续爬取的URL格式，支持正则
    #                        callback='parse_item',   # 用于解析网页的回调函数名
    #                        follow=True
    #     ),
    # )

    def parse(self, response):
        # 通过XPath获取Dom元素
        print("==========================start=============================")
        links = response.xpath("//table[@class='MsoNormalTable']//a/@href").extract()
        for link in links:
            #item = ZkrxItem()
            # item['title'] = link.xpath("//td[@class = 'excel4']/text()").extract()[0]
            # item['content'] = link.xpath("//td[@class = 'excel3']/text()").extract()[0]
            
            yield scrapy.Request(link, callback = self.get_data)

    def get_data(self, response):
        item = ZkrxItem()
        item['title1'] = response.xpath("//body/table[1]//table[1]//td[@class = 'excel4']/text()").extract()[0]
        item['content1'] = response.xpath("//body/table[1]//table[1]/tr/td/text()").extract()[0]
        item['title2'] = response.xpath("//body/table[1]//table[2]//td[@class = 'excel4']/text()").extract()[0]
        item['content2'] = response.xpath("//body/table[1]/table[2]/tr/td/text()").extract()[0]
        
        yield item

    # def parse_item(self, response):
    #     # 通过XPath获取Dom元素
    #     articles = response.xpath("//article")
    #     for article in articles:
    #         item = ZkrxItem()
    #         item['title'] = article.xpath('header/h2/a/text()').extract()[0]
    #         item['url'] = article.xpath('header/h2/a/@href').extract()[0]
    #         item['summary'] = article.xpath('div/p/text()').extract()[0]
    #         yield item