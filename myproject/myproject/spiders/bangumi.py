# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from myproject.items import MyprojectItem
class BangumiSpider(scrapy.Spider):
    name = "bangumi"
    allowed_domains = ["bangumi.tv"]
    start_urls = (
        'http://bangumi.tv/anime/browser?sort=rank',
    )
#    custom_settings
#    crawler
#    settings
#    logger
#==============================================================================
# 
#==============================================================================
#    def from_crawler(crawler, *args, **kwargs):
#    def start_requests():
#    make_requests_from_url(url):
    
    def parse(self, response):
        l = ItemLoader(item=MyprojectItem(), response=response)
        l.add_xpath('name','//li/div[@class="inner"]/h3/a/text()')
        l.add_xpath('link','//li/div[@class="inner"]/h3/a/@href')
        l.add_xpath('score','//li/div[@class="inner"]/p[@class="rateInfo"]/small/text()')
        l.load_item()
        return {
                'name':l.item['name'],
                'link':l.item['link'],
                'score':l.item['score'],
        }
        
#            yield {
#                    'name':sel.xpath('h3/a/text()').extract(),
#                    'link':sel.xpath('h3/a/@href').extract(),
#                    'score':sel.xpath('p[@class="rateInfo"]/small/text()').extract(),
#            }

        
#        filename = response.url.split('/')[-2]
#        with open(filename + '.html','wb') as f:
#            f.write(response.body)
#        
#    def log(message[, level, component]):
#    def closed(reason):
        
