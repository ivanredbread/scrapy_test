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
        for sel in response.xpath('//li/div[@class="inner"]'):
            item = MyprojectItem()
            item['name']  = sel.xpath('h3/a/text()').extract()
            item['link']  = sel.xpath('h3/a/@href').extract()
            item['score'] = sel.xpath('p[@class="rateInfo"]/small/text()').extract()
            item['num']   = sel.xpath('p[@class="rateInfo"]/span/text()').extract()
            item['info']  = sel.xpath('p[@class="info tip"]/text()').extract()
            yield item

        next_page = response.xpath('//div[@class="page_inner"]/strong/text()')
        next_page = str(int(next_page[0].extract())+1)
        if int(next_page) ==80:
            next_page = False
        if next_page:
          url = response.urljoin('http://bangumi.tv/anime/browser?sort=rank&page=' + next_page)
          yield scrapy.Request(url, self.parse)
#------------------------------------------------------------------------------
#    def parse_item(self, response):


#        filename = response.url.split('/')[-2]
#        with open(filename + '.html','wb') as f:
#            f.write(response.body)
#
#    def log(message[, level, component]):
#    def closed(reason):
