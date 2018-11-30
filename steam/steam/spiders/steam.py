# 20171115-steam games rank
#1615--
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from steam.items import SteamItem

class MyCrawlSpider(CrawlSpider):
    name = 'steam_spider'               # Spider名，必须唯一，执行爬虫命令时使用
    allowed_domains = ['store.steampowered.com']   # 限定允许爬的域名，可设置多个
    start_urls = [
        # "http://store.steampowered.com/games/",       # 种子URL，可设置多个
        "http://store.steampowered.com/app/410900/Forts/",

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

        # links = response.xpath("//table[@class='MsoNormalTable']//a/@href").extract()
        # for link in links:
        #     #item = ZkrxItem()
        #     # item['title'] = link.xpath("//td[@class = 'excel4']/text()").extract()[0]
        #     # item['content'] = link.xpath("//td[@class = 'excel3']/text()").extract()[0]
            
        #     yield scrapy.Request(link, callback = self.get_data)
        item = SteamItem()
        item['gameName'] = response.xpath("//div[@class = 'apphub_AppName']/text()").extract()[0]
        item['gameType'] = response.xpath("//div[@class = 'breadcrumbs']/div/a[1]/text()").extract()[0]
        item['gameScore'] = response.xpath("//div[@class = 'glance_ctn_responsive_left']/div[@class ='user_reviews']/div[1]/span[@class ='nonresponsive_hidden responsive_reviewdesc']/text()").extract()[0]
        item['gameIntro'] = response.xpath("//div[@class ='game_description_snippet']/text()").extract()[0]
        item['gamePrice'] = response.xpath("//div[@class = 'game_purchase_price price']/text()").extract()[0]
        item['gameTags'] = response.xpath("//div[@class = 'glance_tags popular_tags']/a").extract()[0]
        item['gamePlayersNum'] = response.xpath("//div[@class = 'block responsive_apppage_details_left']").extract()[0]
        yield item

    def get_data(self, response):
        # item = SteamItem()
        # item['gameName'] = response.xpath("//div[@class = 'apphub_AppName']/text()").extract()[0]
        # item['gameType'] = response.xpath("//div[@class = 'breadcrumbs']/div/a[1]/text()").extract()[0]
        # item['gameScore'] = response.xpath("//div[@class = 'glance_ctn_responsive_left']/div[@class ='user_reviews']/div[1]/span[@class ='nonresponsive_hidden responsive_reviewdesc']/text()").extract()[0]
        # item['gameIntro'] = response.xpath("//div[@class ='game_description_snippet']/text()").extract()[0]
        # item['gamePrice'] = response.xpath("//div[@class = 'game_purchase_price price']/text()").extract()[0]
        # item['gameTags'] = response.xpath("//div[@class = 'glance_tags popular_tags']/a").extract()[0]
        # item['gamePlayersNum'] = response.xpath("//div[@class = 'block responsive_apppage_details_left']").extract()[0]
        # yield item

    # def parse_item(self, response):
    #     # 通过XPath获取Dom元素
    #     articles = response.xpath("//article")
    #     for article in articles:
    #         item = ZkrxItem()
    #         item['title'] = article.xpath('header/h2/a/text()').extract()[0]
    #         item['url'] = article.xpath('header/h2/a/@href').extract()[0]
    #         item['summary'] = article.xpath('div/p/text()').extract()[0]
    #         yield item