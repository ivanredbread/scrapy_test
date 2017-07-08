# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 11:24:01 2017

@author: tedoreve
"""

# -*- coding: utf-8 -*-
import scrapy
#from scrapy.loader import ItemLoader
from myproject.items import BilibiliItem

class BilibiliSpider(scrapy.Spider):
    name = "bilibili"
    allowed_domains = ["bilibili.com"]
    start_urls = (
    "http://api.bilibili.com/archive_stat/stat?aid=7",
    )

#    custom_settings
#    crawler
#    settings
#    logger
#==============================================================================
#
#==============================================================================
#    def from_crawler(crawler, *args, **kwargs):
#    def start_requests(self):
#        url_head = 'http://bangumi.tv/anime/browser?sort=rank&page='
#        for line in range(21):
#            self.start_urls.append(url_head + str(line+1))
#    make_requests_from_url(url):
#------------------------------------------------------------------------------
    def parse(self, response):
#------------------------------the first method--------------------------------
#        l = ItemLoader(item=MyprojectItem(), response=response)
#        l.add_xpath('name','//li/div[@class="inner"]/h3/a/text()')
#        l.add_xpath('link','//li/div[@class="inner"]/h3/a/@href')
#        l.add_xpath('score','//li/div[@class="inner"]/p[@class="rateInfo"]/small/text()')
#        l.load_item()
#        return {
#                'name':l.item['name'],
#                'link':l.item['link'],
#                'score':l.item['score'],
#        }
#------------------------------the second method-------------------------------
#        for sel in response.xpath('//li/div[@class="inner"]'):
#            yield {
#                    'name':sel.xpath('h3/a/text()').extract(),
#                    'link':sel.xpath('h3/a/@href').extract(),
#                    'score':sel.xpath('p[@class="rateInfo"]/small/text()').extract(),
#            }
#------------------------------the third method--------------------------------
#        for sel in response.xpath('//div[@class="b-page-body"]/div[@class="main-inner"]/div[@class="viewbox report-scroll-module"]/div[@class="info"]'):
        item = BilibiliItem()
        item['link']    = response.url
        item['source']  = response.text
        
#            item['link']  = sel.xpath('div[@class="v-title"]/h1/text()').extract()
#            item['time']  = sel.xpath('div[@class="tminfo"]/time/i/text()').extract()
#            item['play']  = sel.xpath('div[@class="v-title-info"]/div[@class="v-title-line"]/span[@id="dianji"]/text()').extract()
#            item['danmu'] = sel.xpath('div[@class="v-title"]/h1/text()').extract()
#            try:
#                item['rank']  = sel.xpath('div[@class="v-title-info"]/div[@class="v-title-line v-rank"]/span/text()').extract()
#            except:
#                item['rank']  = "zhazha"
#            item['coins'] = sel.xpath('div[@class="v-title"]/h1/text()').extract()
#            item['favo']  = sel.xpath('div[@class="v-title"]/h1/text()').extract()
#            item['link']  = sel.xpath('h3/a/@href').extract()
#            item['score'] = sel.xpath('p[@class="rateInfo"]/small/text()').extract()
#            item['num']   = sel.xpath('p[@class="rateInfo"]/span/text()').extract()
#            item['info']  = sel.xpath('p[@class="info tip"]/text()').extract()
        yield item

        for i in range(11766441):
            url = response.urljoin("http://api.bilibili.com/archive_stat/stat?aid="+str(i+8))
            yield scrapy.Request(url, self.parse)
#------------------------------------------------------------------------------
#    def parse_item(self, response):


#        filename = response.url.split('/')[-2]
#        with open(filename + '.html','wb') as f:
#            f.write(response.body)
#
#    def log(message[, level, component]):
#    def closed(reason):
